import axios from 'axios'

// 豆包大模型API配置
const DOUBAO_API_KEY = '161ec8aa-2cb6-4c30-add2-e34ec5e0a94b' // 请替换为您的API密钥
const DOUBAO_MODEL = 'doubao-1-5-thinking-vision-pro-250428'
const DOUBAO_BASE_URL = 'https://ark.cn-beijing.volces.com/api/v3'

// 创建axios实例
const doubaoApi = axios.create({
  baseURL: DOUBAO_BASE_URL,
  headers: {
    'Authorization': `Bearer ${DOUBAO_API_KEY}`,
    'Content-Type': 'application/json'
  },
  timeout: 30000
})

/**
 * 将文件转换为base64格式
 */
const fileToBase64 = (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = () => {
      const base64 = reader.result.split(',')[1] // 移除data:image/...;base64,前缀
      resolve(base64)
    }
    reader.onerror = reject
    reader.readAsDataURL(file)
  })
}

/**
 * 豆包大模型分析服务
 */
export const doubaoAnalysisService = {
  /**
   * 分析服装图片
   * @param {File} imageFile - 图片文件
   * @returns {Promise<Object>} 结构化的分析结果
   */
  async analyzeImage(imageFile) {
    try {
      const base64Image = await fileToBase64(imageFile)
      
      const requestData = {
        model: DOUBAO_MODEL,
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'text',
                text: `请对这张服装图片进行详细的时尚分析。请严格按照以下JSON格式返回结果，不要添加任何额外的解释或说明文字：

{
  "style_and_type": ["服装风格", "服装类型", "材质", "其他标签"],
  "color_theme": ["主要颜色1的HEX代码", "主要颜色2的HEX代码", "主要颜色3的HEX代码"],
  "pairing_suggestions": "详细的搭配建议，包括配饰、鞋子、发型等。",
  "suitable_occasions": "这套服装适合的场合和活动。"
}`
              },
              {
                type: 'image_url',
                image_url: {
                  url: `data:image/jpeg;base64,${base64Image}`
                }
              }
            ]
          }
        ],
        max_tokens: 2000,
        temperature: 0.7
      }

      const response = await doubaoApi.post('/chat/completions', requestData)
      
      if (response.data && response.data.choices && response.data.choices[0]) {
        const content = response.data.choices[0].message.content
        
        // 提取JSON字符串
        const jsonMatch = content.match(/\{([\s\S]*?)\}/)
        if (jsonMatch) {
          const jsonString = jsonMatch[0]
          const parsedResult = JSON.parse(jsonString)
          return parsedResult
        } else {
          throw new Error('AI模型未返回有效的JSON格式')
        }
      } else {
        throw new Error('API响应格式错误')
      }
    } catch (error) {
      console.error('豆包API调用或解析失败:', error)
      
      if (error.response) {
        const { status, data } = error.response
        const message = data?.error?.message || '服务器错误'
        if (status === 401) throw new Error('API密钥无效')
        if (status === 429) throw new Error('请求频繁，请稍后再试')
        if (status === 400) throw new Error('请求参数错误')
        throw new Error(`服务器错误: ${message}`)
      } else if (error.request) {
        throw new Error('网络连接失败，请检查网络')
      } else {
        throw new Error(`分析失败: ${error.message}`)
      }
    }
  }
}

export default doubaoAnalysisService
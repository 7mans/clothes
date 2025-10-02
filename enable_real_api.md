# 启用真实大模型 API 调用指南

## 1. 安装必要依赖

```bash
pip install volcenginesdkarkruntime tos
```

## 2. 配置环境变量

在 `.env` 文件中添加：

```env
# 豆包API配置
ARK_API_KEY=your_ark_api_key_here
DOUBAO_MODEL_ID=ep-20241224075001-xxxxx

# 火山引擎配置
VOLC_ACCESSKEY=your_volc_access_key_here
VOLC_SECRETKEY=your_volc_secret_key_here

# TOS存储配置
TOS_ENDPOINT=tos-cn-beijing.volces.com
TOS_REGION=cn-beijing
TOS_BUCKET_NAME=ai2cloth-images
```

## 3. 修改 AI 服务调用逻辑

将 `ai_service.py` 中的模拟调用替换为真实调用：

```python
async def analyze_clothing_image(self, image_path: str) -> Optional[Dict]:
    try:
        print(f"开始分析图片: {image_path}")

        # 使用豆包视觉服务进行真实分析
        result = await self.doubao_vision.analyze_clothing_image(image_path)

        if result:
            print(f"分析成功，类型: {result.get('clothing_type')}")
            return result
        else:
            print("分析失败，使用模拟数据")
            return self._mock_analysis_result()

    except Exception as e:
        print(f"图片分析错误: {e}")
        return self._mock_analysis_result()
```

## 4. 测试 API 调用

运行测试脚本验证 API 调用：

```bash
python3 test_real_api.py
```

<template>
  <div class="analysis-page">
    <!-- 导航栏 -->
    <Header />
    
    <!-- 返回按钮 -->
    <div class="back-button" @click="goBack">
      <i class="fas fa-arrow-left"></i>
      {{ $t('analysis.backToHome') }}
    </div>
    
    <!-- 主要内容区域 -->
    <div class="main-content">
      <div class="analysis-container">
        <h1 class="page-title">{{ $t('analysis.title') }}</h1>
        <p class="page-subtitle">{{ $t('analysis.subtitle') }}</p>
        
        <!-- 分析工具容器 -->
        <div v-if="!uploadedImage && !analyzing" class="analysis-tool-container">
          <!-- 上传区域 -->
          <div class="upload-area">
            <div 
              class="upload-zone" 
              :class="{ 'drag-over': dragOver }"
              @drop="handleDrop"
              @dragover.prevent="dragOver = true"
              @dragleave="dragOver = false"
              @click="triggerFileInput"
            >
              <div class="upload-content">
                <div class="upload-icon">
                  <i class="fas fa-cloud-upload-alt"></i>
                </div>
                <h3>{{ $t('analysis.upload.title') }}</h3>
                <p>{{ $t('analysis.upload.subtitle') }}</p>
              </div>
            </div>
            <input 
              ref="fileInput" 
              type="file" 
              accept="image/*" 
              @change="handleFileSelect" 
              style="display: none"
            >
          </div>
          
          <!-- 搜索框样式的输入区域 -->
          <div class="search-container">
            <div class="search-box">
              <input 
                v-model="analysisDescription"
                type="text" 
                class="search-input"
                placeholder="请输入您想要分析的具体内容，如：搭配建议、风格分析、颜色搭配等..."
                maxlength="200"
                @keyup.enter="triggerFileInput"
              >
              <button 
                class="search-button"
                @click="triggerFileInput"
                title="开始AI分析"
              >
                <i class="fas fa-search"></i>
              </button>
            </div>
            <div class="search-hint">可选：描述您的分析需求，获得更精准的建议</div>
          </div>
        </div>
        
        <!-- 图片预览和分析状态 -->
        <div v-if="uploadedImage" class="image-preview-section">
          <div class="analysis-tool-container">
            <div class="image-container">
              <img :src="uploadedImage" alt="上传的图片" class="preview-image">
              <button v-if="!analyzing" class="remove-image" @click="removeImage">
                <i class="fas fa-times"></i>
              </button>
            </div>
            
            <!-- 分析中状态 -->
            <div v-if="analyzing" class="analyzing-status">
              <div class="loading-spinner"></div>
              <h3>{{ $t('analysis.analyzing.title') }}</h3>
              <p>{{ $t('analysis.analyzing.subtitle') }}</p>
            </div>
            
            <!-- 输入框和分析按钮 -->
            <div v-if="!analyzing && !analysisResult" class="analysis-controls">
              <!-- 搜索框样式的输入区域 -->
              <div class="search-container">
                <div class="search-box">
                  <input 
                    v-model="analysisDescription"
                    type="text" 
                    class="search-input"
                    placeholder="请输入您想要分析的具体内容，如：搭配建议、风格分析、颜色搭配等..."
                    maxlength="200"
                    @keyup.enter="startAnalysis"
                  >
                  <button 
                    class="search-button"
                    @click="startAnalysis"
                    title="开始AI分析"
                  >
                    <i class="fas fa-search"></i>
                  </button>
                </div>
                <div class="search-hint">可选：描述您的分析需求，获得更精准的建议</div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 分析结果 -->
        <div v-if="analysisResult" class="analysis-result">
          <AnalysisResult :result="analysisResult" :image="uploadedImage" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import AnalysisResult from '@/components/AnalysisResult.vue'
import { doubaoAnalysisService } from '@/services/doubaoService'

export default {
  name: 'Analysis',
  components: {
    Header,
    AnalysisResult
  },
  data() {
    return {
      uploadedImage: null,
      uploadedFile: null,
      analyzing: false,
      analysisResult: null,
      dragOver: false,
      error: null,
      analysisDescription: ''
    }
  },
  methods: {
    goBack() {
      this.$router.push('/')
    },
    
    triggerFileInput() {
      this.$refs.fileInput.click()
    },
    
    handleFileSelect(event) {
      const file = event.target.files[0]
      if (file) {
        this.processFile(file)
      }
    },
    
    handleDrop(event) {
      event.preventDefault()
      this.dragOver = false
      
      const files = event.dataTransfer.files
      if (files.length > 0) {
        this.processFile(files[0])
      }
    },
    
    processFile(file) {
      // 验证文件类型
      if (!file.type.startsWith('image/')) {
        alert(this.$t('analysis.errors.invalidFile'))
        return
      }
      
      // 验证文件大小 (10MB)
      if (file.size > 10 * 1024 * 1024) {
        alert(this.$t('analysis.errors.fileTooLarge'))
        return
      }
      
      this.uploadedFile = file
      
      // 创建预览
      const reader = new FileReader()
      reader.onload = (e) => {
        this.uploadedImage = e.target.result
      }
      reader.readAsDataURL(file)
    },
    
    removeImage() {
      this.uploadedImage = null
      this.uploadedFile = null
      this.analysisResult = null
      this.error = null
    },
    
    async startAnalysis() {
      if (!this.uploadedFile) return
      
      this.analyzing = true
      this.error = null
      
      try {
        const result = await doubaoAnalysisService.analyzeImage(this.uploadedFile)
        this.analysisResult = result
      } catch (error) {
        console.error('分析失败:', error)
        this.error = this.$t('analysis.errors.analysisFailed')
        alert(this.$t('analysis.errors.analysisFailed'))
      } finally {
        this.analyzing = false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.analysis-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  color: #1a1a1a;
  position: relative;
  overflow-x: hidden;
  
  // 添加动态背景效果
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
      radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.05) 0%, transparent 50%),
      radial-gradient(circle at 80% 20%, rgba(59, 130, 246, 0.03) 0%, transparent 50%),
      radial-gradient(circle at 40% 40%, rgba(59, 130, 246, 0.02) 0%, transparent 50%);
    pointer-events: none;
    animation: backgroundFloat 20s ease-in-out infinite;
  }
}

@keyframes backgroundFloat {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
    opacity: 1;
  }
  50% { 
    transform: translateY(-20px) rotate(1deg); 
    opacity: 0.8;
  }
}

.back-button {
  position: fixed;
  top: 80px;
  left: 24px;
  display: flex;
  align-items: center;
  gap: 8px;
  color: #666666;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  padding: 10px 16px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(0, 0, 0, 0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 100;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  
  &:hover {
    color: #1a1a1a;
    background: rgba(255, 255, 255, 1);
    transform: translateX(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  }
  
  i {
    font-size: 12px;
    transition: transform 0.3s ease;
  }
  
  &:hover i {
    transform: translateX(-2px);
  }
}

.main-content {
  padding-top: 80px;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 1;
}

.analysis-container {
  max-width: 900px;
  width: 100%;
  padding: 60px 24px;
  text-align: center;
}

.page-title {
  font-size: 48px;
  font-weight: 800;
  margin: 0 0 20px 0;
  background: linear-gradient(135deg, #1a1a1a 0%, #374151 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.page-subtitle {
  font-size: 18px;
  color: #666666;
  margin: 0 0 80px 0;
  font-weight: 400;
  line-height: 1.6;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 80px;
}

// 分析工具容器样式
.analysis-tool-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 40px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
  border: 2px solid rgba(59, 130, 246, 0.2);
  position: relative;
  overflow: hidden;
  margin-bottom: 50px;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(147, 197, 253, 0.05) 100%);
    pointer-events: none;
  }
  
  &::after {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(135deg, #3b82f6, #60a5fa, #93c5fd);
    border-radius: 26px;
    z-index: -1;
    opacity: 0.8;
  }
}

.upload-area {
  margin-bottom: 30px;
  position: relative;
  z-index: 1;
}

.upload-zone {
  border: 2px dashed #d1d5db;
  border-radius: 20px;
  padding: 60px 40px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
    transition: left 0.6s;
  }
  
  &:hover, &.drag-over {
    border-color: #3b82f6;
    background: rgba(255, 255, 255, 0.8);
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    
    &::before {
      left: 100%;
    }
  }
}

.upload-content {
  position: relative;
  z-index: 1;
  
  .upload-icon {
    font-size: 48px;
    margin-bottom: 16px;
    color: #3b82f6;
  }
  
  h3 {
    font-size: 20px;
    font-weight: 600;
    margin: 0 0 12px 0;
    line-height: 1.3;
    color: #1a1a1a;
  }
  
  p {
    font-size: 14px;
    color: #666666;
    margin: 0;
    font-weight: 400;
  }
}

// 百度搜索样式的搜索容器
.search-container {
  margin: 30px 0;
  position: relative;
  z-index: 1;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.search-box {
  display: flex;
  align-items: center;
  background: #ffffff;
  border: 2px solid #c4c7ce;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  
  &:hover {
    border-color: #4e6ef2;
    box-shadow: 0 2px 15px rgba(78, 110, 242, 0.15);
  }
  
  &:focus-within {
    border-color: #4e6ef2;
    box-shadow: 0 2px 15px rgba(78, 110, 242, 0.2);
  }
}

.search-input {
  flex: 1;
  padding: 16px 20px;
  border: none;
  outline: none;
  font-size: 16px;
  color: #222;
  background: transparent;
  
  &::placeholder {
    color: #999;
    font-size: 14px;
  }
}

.search-button {
  background: #4e6ef2;
  border: none;
  padding: 16px 20px;
  cursor: pointer;
  color: white;
  font-size: 16px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 60px;
  
  &:hover {
    background: #3b5bdb;
  }
  
  &:active {
    background: #364fc7;
    transform: scale(0.98);
  }
  
  i {
    font-size: 16px;
  }
}

.search-hint {
  font-size: 12px;
  color: #666;
  margin-top: 8px;
  text-align: center;
}

// 分析控制区域
.analysis-controls {
  position: relative;
  z-index: 1;
}

.image-preview-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
  
  .analysis-tool-container {
    width: 100%;
    max-width: 600px;
  }
}

.image-container {
  position: relative;
  max-width: 500px;
  width: 100%;
}

.preview-image {
  width: 100%;
  height: auto;
  max-height: 600px;
  object-fit: contain;
  border-radius: 20px;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.remove-image {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 40px;
  height: 40px;
  background: rgba(0, 0, 0, 0.7);
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(10px);
  
  &:hover {
    background: rgba(0, 0, 0, 0.9);
    transform: scale(1.1);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  }
}

.analyzing-status {
  text-align: center;
  padding: 40px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  backdrop-filter: blur(20px);
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  
  h3 {
    font-size: 24px;
    font-weight: 600;
    margin: 24px 0 12px 0;
    color: #1a1a1a;
  }
  
  p {
    font-size: 16px;
    color: #666666;
    margin: 0;
  }
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(59, 130, 246, 0.2);
  border-top: 4px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.analyze-button {
  background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
  color: #3b82f6;
  border: none;
  padding: 18px 40px;
  border-radius: 30px;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
    transition: left 0.6s;
  }
  
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    
    &::before {
      left: 100%;
    }
  }
  
  &:active {
    transform: translateY(-1px);
  }
}

.analysis-result {
  margin-top: 60px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 24px;
  padding: 40px;
  backdrop-filter: blur(20px);
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

// 响应式设计
@media (max-width: 768px) {
  .back-button {
    top: 70px;
    left: 16px;
    font-size: 13px;
    padding: 8px 14px;
  }
  
  .analysis-container {
    padding: 40px 20px;
  }
  
  .page-title {
    font-size: 36px;
  }
  
  .page-subtitle {
    font-size: 16px;
    margin-bottom: 60px;
  }
  
  .analysis-tool-container {
    padding: 30px 20px;
    margin-bottom: 40px;
  }
  
  .upload-zone {
    padding: 50px 20px;
  }
  
  .upload-content {
    .upload-icon {
      font-size: 40px;
    }
    
    h3 {
      font-size: 18px;
    }
    
    p {
      font-size: 13px;
    }
  }
  
  .search-container {
    margin: 25px 0;
  }
  
  .search-box {
    border-radius: 8px;
  }
  
  .search-input {
    padding: 14px 16px;
    font-size: 14px;
    
    &::placeholder {
      font-size: 13px;
    }
  }
  
  .search-button {
    padding: 14px 16px;
    min-width: 50px;
    font-size: 14px;
    
    i {
      font-size: 14px;
    }
  }
  
  .search-hint {
    font-size: 11px;
  }
  
  .preview-image {
    max-height: 450px;
  }
  
  .analyzing-status {
    padding: 30px 20px;
    
    h3 {
      font-size: 20px;
    }
    
    p {
      font-size: 14px;
    }
  }
}

@media (max-width: 480px) {
  .main-content {
    padding-top: 60px;
  }
  
  .analysis-container {
    padding: 30px 16px;
  }
  
  .page-title {
    font-size: 28px;
  }
  
  .analysis-tool-container {
    padding: 25px 16px;
    margin-bottom: 30px;
  }
  
  .upload-zone {
    padding: 40px 16px;
  }
  
  .upload-content {
    .upload-icon {
      font-size: 36px;
    }
    
    h3 {
      font-size: 16px;
    }
    
    p {
      font-size: 12px;
    }
  }
  
  .search-container {
    margin: 20px 0;
  }
  
  .search-box {
    border-radius: 6px;
  }
  
  .search-input {
    padding: 12px 14px;
    font-size: 13px;
    
    &::placeholder {
      font-size: 12px;
    }
  }
  
  .search-button {
    padding: 12px 14px;
    min-width: 45px;
    font-size: 13px;
    
    i {
      font-size: 13px;
    }
  }
  
  .search-hint {
    font-size: 10px;
  }
}
</style>
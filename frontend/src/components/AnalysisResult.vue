<template>
  <div class="analysis-result">
    <div class="result-header">
      <h2 class="heading-3">AI 时尚分析报告</h2>
      <p>基于您上传的图片生成的专业分析</p>
    </div>

    <div class="result-body">
      <div class="result-image-container">
        <img :src="image" alt="分析的图片" class="result-image">
      </div>

      <div class="result-details">
        <!-- 风格分析 -->
        <div class="result-section">
          <div class="section-title">
            <i class="fas fa-tshirt"></i>
            <h3>风格与类型</h3>
          </div>
          <div class="tags">
            <span class="tag" v-for="tag in result.style_and_type" :key="tag">{{ tag }}</span>
          </div>
        </div>

        <!-- 颜色分析 -->
        <div class="result-section">
          <div class="section-title">
            <i class="fas fa-palette"></i>
            <h3>颜色主题</h3>
          </div>
          <div class="color-palette">
            <div 
              class="color-swatch"
              v-for="color in result.color_theme" 
              :key="color"
              :style="{ backgroundColor: color }"
              :title="color"
            ></div>
          </div>
        </div>

        <!-- 搭配建议 -->
        <div class="result-section">
          <div class="section-title">
            <i class="fas fa-lightbulb"></i>
            <h3>搭配建议</h3>
          </div>
          <p class="suggestion-text">{{ result.pairing_suggestions }}</p>
        </div>

        <!-- 场合推荐 -->
        <div class="result-section">
          <div class="section-title">
            <i class="fas fa-calendar-check"></i>
            <h3>适合场合</h3>
          </div>
          <p class="suggestion-text">{{ result.suitable_occasions }}</p>
        </div>
      </div>
    </div>

    <div class="result-footer">
      <button class="btn btn-secondary" @click="$emit('close')">
        <i class="fas fa-times"></i>
        关闭
      </button>
      <button class="btn btn-primary">
        <i class="fas fa-shopping-cart"></i>
        发现相似单品
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnalysisResult',
  props: {
    result: {
      type: Object,
      required: true
    },
    image: {
      type: String,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
.analysis-result {
  padding: var(--spacing-2xl);
  width: 800px;
}

.result-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);

  h2 {
    background: var(--gradient-accent);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: var(--spacing-sm);
  }

  p {
    color: var(--color-text-secondary);
    font-size: var(--font-size-lg);
  }
}

.result-body {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-2xl);
}

.result-image-container {
  .result-image {
    width: 100%;
    height: auto;
    border-radius: var(--radius-xl);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-lg);
  }
}

.result-details {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xl);
}

.result-section {
  background: var(--color-bg-secondary);
  padding: var(--spacing-lg);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);

  .section-title {
    display: flex;
    align-items: center;
    gap: var(--spacing-md);
    margin-bottom: var(--spacing-md);
    color: var(--color-text-primary);

    i {
      color: var(--color-accent);
      font-size: 18px;
    }

    h3 {
      margin: 0;
      font-size: var(--font-size-lg);
      font-weight: var(--font-weight-semibold);
    }
  }
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-sm);

  .tag {
    background: var(--color-accent-light);
    color: var(--color-accent);
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--radius-md);
    font-size: var(--font-size-sm);
    font-weight: var(--font-weight-medium);
  }
}

.color-palette {
  display: flex;
  gap: var(--spacing-sm);

  .color-swatch {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid var(--color-border-light);
    box-shadow: var(--shadow-sm);
  }
}

.suggestion-text {
  color: var(--color-text-secondary);
  line-height: 1.7;
  margin: 0;
}

.result-footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--spacing-md);
  padding-top: var(--spacing-xl);
  border-top: 1px solid var(--color-border);
}

@media (max-width: 768px) {
  .analysis-result {
    width: auto;
    padding: var(--spacing-lg);
  }

  .result-body {
    grid-template-columns: 1fr;
  }
}
</style>
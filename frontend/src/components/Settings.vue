<template>
  <div class="settings-container">
    <h2 class="settings-title">设置</h2>

    <div class="setting-group">
      <h3 class="group-title">外观</h3>
      
      <!-- 字体大小设置 -->
      <div class="setting-item">
        <label for="font-size-select">字体大小</label>
        <div class="select-wrapper">
          <select id="font-size-select" :value="fontSize" @change="updateFontSize">
            <option value="small">小</option>
            <option value="medium">中</option>
            <option value="large">大</option>
            <option value="extra-large">超大</option>
          </select>
        </div>
      </div>

      <!-- 字体类型设置 -->
      <div class="setting-item">
        <label for="font-family-select">字体</label>
        <div class="select-wrapper">
          <select id="font-family-select" :value="fontFamily" @change="updateFontFamily">
            <option value="default">默认</option>
            <option value="serif">衬线体</option>
            <option value="sans-serif">非衬线体</option>
            <option value="monospace">等宽字体</option>
          </select>
        </div>
      </div>
    </div>

    <div class="setting-group">
      <h3 class="group-title">关于</h3>
      <div class="about-section">
        <p><strong>时尚AI分析助手</strong></p>
        <p>版本: 1.0.0</p>
        <p>一个使用Vue.js和FastAPI构建的智能时尚分析工具。</p>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Settings',
  props: {
    fontSize: {
      type: String,
      required: true
    },
    fontFamily: {
      type: String,
      required: true
    }
  },
  methods: {
    updateFontSize(event) {
      this.$emit('update:fontSize', event.target.value);
    },
    updateFontFamily(event) {
      this.$emit('update:fontFamily', event.target.value);
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/styles/global.scss';

.settings-container {
  padding: $spacing-xl;
  height: 100%;
  overflow-y: auto;
  background-color: $color-bg-main;

  .settings-title {
    font-size: $font-size-2xl;
    font-weight: 600;
    color: $color-text-primary;
    margin-bottom: $spacing-lg;
    border-bottom: 2px solid $color-primary;
    padding-bottom: $spacing-sm;
  }
}

.setting-group {
  margin-bottom: $spacing-xl;

  .group-title {
    font-size: $font-size-lg;
    font-weight: 600;
    color: $color-text-secondary;
    margin-bottom: $spacing-base;
  }
}

.setting-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: $spacing-base;
  padding: $spacing-base;
  background-color: $color-white;
  border-radius: $border-radius-base;
  border: 1px solid $color-border;

  label {
    font-size: $font-size-base;
    color: $color-text-primary;
  }

  .select-wrapper {
    position: relative;
    display: inline-block;

    select {
      -webkit-appearance: none;
      -moz-appearance: none;
      appearance: none;
      background-color: $color-bg-main;
      border: 1px solid $color-border;
      padding: $spacing-sm $spacing-lg $spacing-sm $spacing-base;
      border-radius: $border-radius-base;
      cursor: pointer;
      font-size: $font-size-base;
      min-width: 150px;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;

      &:hover {
        border-color: $color-primary;
      }

      &:focus {
        outline: none;
        border-color: $color-primary;
        box-shadow: 0 0 0 2px rgba($color-primary, 0.2);
      }
    }

    &::after {
      content: '▼';
      font-size: 12px;
      color: $color-text-muted;
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
    }
  }
}

.about-section {
  background-color: $color-white;
  padding: $spacing-base;
  border-radius: $border-radius-base;
  border: 1px solid $color-border;
  font-size: $font-size-base;
  color: $color-text-secondary;

  p {
    margin: 0 0 $spacing-sm 0;
    line-height: 1.6;

    strong {
      color: $color-text-primary;
    }
  }
}
</style>

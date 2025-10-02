import zh from './zh.js'
import en from './en.js'

class I18n {
  constructor() {
    this.currentLanguage = 'zh'
    this.messages = {
      zh,
      en
    }
  }

  setLanguage(lang) {
    if (this.messages[lang]) {
      this.currentLanguage = lang
      // 保存到本地存储
      localStorage.setItem('language', lang)
      // 触发语言变更事件
      window.dispatchEvent(new CustomEvent('languageChanged', { detail: lang }))
    }
  }

  getCurrentLanguage() {
    return this.currentLanguage
  }

  t(key) {
    const keys = key.split('.')
    let value = this.messages[this.currentLanguage]
    
    for (const k of keys) {
      if (value && typeof value === 'object') {
        value = value[k]
      } else {
        return key // 如果找不到翻译，返回原key
      }
    }
    
    return value || key
  }

  // 初始化语言设置
  init() {
    const savedLanguage = localStorage.getItem('language')
    if (savedLanguage && this.messages[savedLanguage]) {
      this.currentLanguage = savedLanguage
    }
  }
}

// 创建全局实例
const i18n = new I18n()
i18n.init()

export default i18n

import i18n from '../i18n'

export default {
  install(Vue) {
    // 添加全局属性
    Vue.prototype.$i18n = i18n
    Vue.prototype.$t = (key) => i18n.t(key)
    
    // 添加全局混入，监听语言变化
    Vue.mixin({
      data() {
        return {
          currentLanguage: i18n.getCurrentLanguage()
        }
      },
      mounted() {
        // 监听语言变化事件
        window.addEventListener('languageChanged', this.handleLanguageChange)
      },
      beforeDestroy() {
        window.removeEventListener('languageChanged', this.handleLanguageChange)
      },
      methods: {
        handleLanguageChange(event) {
          this.currentLanguage = event.detail
          this.$forceUpdate()
        }
      }
    })
  }
}

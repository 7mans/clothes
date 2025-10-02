import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Import global styles
import './styles/global.scss'

// Import Font Awesome
import '@fortawesome/fontawesome-free/css/all.css'

// Import i18n plugin
import I18nPlugin from './plugins/i18n'

Vue.config.productionTip = false

// Use i18n plugin
Vue.use(I18nPlugin)

// Create and mount the Vue application
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
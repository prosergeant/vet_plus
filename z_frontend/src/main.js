import 'core-js/stable'
import Vue from 'vue'
import App from './App'
import router from './router'
import CoreuiVue from '@coreui/vue'
import { iconsSet as icons } from './assets/icons/icons.js'
import store from './store'
import Axios from 'axios'
import '@babel/polyfill'
import VueGeolocation from 'vue-browser-geolocation';
import VueImg from 'v-img';

Vue.use(VueImg);
Vue.use(VueGeolocation);

Vue.config.performance = true
Vue.use(CoreuiVue)
Vue.prototype.$log = console.log.bind(console)
Vue.prototype.$http = Axios


new Vue({
  el: '#app',
  router,
  store,
  icons,
  template: '<App/>',
  components: {
    App
  }
})

import Vue from 'vue'
import 'babel-polyfill'

import App from './App'
import router from './router'
import store from './store'
import Bars from 'vuebars'
import Chartkick from 'chartkick'
import VueChartkick from 'vue-chartkick'
import Highcharts from 'highcharts'

window.Highcharts = Highcharts
Vue.use(VueChartkick, { Chartkick })

Vue.use(Bars)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})

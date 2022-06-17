import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from './axios-api'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    accessToken: localStorage.getItem('token') || '',
    refreshToken: null,
    APIData: '',
    sidebarShow: 'responsive',
    sidebarMinimize: false,
    base_url: 'http://192.168.0.30:8000', // 'http://185.68.21.251',
    current_klass: localStorage.getItem('klass') || null,
    is_auth: localStorage.getItem('is_auth') || false
  },
  mutations: {
    updateKlass(state, {klass}){
      state.current_klass = klass
      localStorage.setItem('klass', klass)
    },
    updateStorage (state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
      localStorage.setItem('token', access)
      localStorage.setItem('is_auth', true)
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('token')
      localStorage.removeItem('is_auth')
    },
    toggleSidebarDesktop (state) {
      const sidebarOpened = [true, 'responsive'].includes(state.sidebarShow)
      state.sidebarShow = sidebarOpened ? false : 'responsive'
    },
    toggleSidebarMobile (state) {
      const sidebarClosed = [false, 'responsive'].includes(state.sidebarShow)
      state.sidebarShow = sidebarClosed ? true : 'responsive'
    },
    set (state, [variable, value]) {
      state[variable] = value
    }
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    }
  },
  actions: {
    userKlass (context, klass) {
      context.commit('updateKlass', {klass: klass.klass})
    },
    userLogout (context) {
      if (context.getters.loggedIn) {
          context.commit('destroyToken')
      }
    },
    userLogin (context, usercredentials) {
      return new Promise((resolve, reject) => {
        getAPI.post('/api/api-token/', {
          email: usercredentials.email,
          password: usercredentials.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh }) 
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    }
  }
})
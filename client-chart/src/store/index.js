import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data_si: [],
    data_tsl: [],
    refreshTime: 3000
  },
  actions: {
    pushDataSi ({ commit }, data) {
      commit('PUSH_DATA_SI', data)
    },
    setDataSi ({ commit }, data) {
      commit('SET_DATA_SI')
    },
    pushDataTsl ({ commit }, data) {
      commit('PUSH_DATA_TSL', data)
    },
    setDataTsl ({ commit }, data) {
      commit('SET_DATA_TSL')
    },
    setRefreshTime ({ commit }, data) {
      commit('SET_REFRESH_TIME', data)
    }
  },
  mutations: {
    PUSH_DATA_SI (state, data) {
      state.data_tsl.push(data)
    },
    SET_DATA_SI (state, data) {
      state.data_si = []
    },
    PUSH_DATA_TSL (state, data) {
      state.data_tsl.push(data)
    },
    SET_DATA_TSL (state, data) {
      state.data_tsl = []
    },
    SET_REFRESH_TIME (state, data) {
      state.refreshTime = data
    }
  },
  plugins: [createPersistedState()]
})

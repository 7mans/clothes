import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
    analysisHistory: [],
    loading: false,
    error: null
  },
  getters: {
    isAuthenticated: state => !!state.token,
    currentUser: state => state.user,
    getAnalysisHistory: state => state.analysisHistory,
    isLoading: state => state.loading,
    getError: state => state.error
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user
    },
    SET_TOKEN(state, token) {
      state.token = token
      if (token) {
        localStorage.setItem('token', token)
      } else {
        localStorage.removeItem('token')
      }
    },
    SET_ANALYSIS_HISTORY(state, history) {
      state.analysisHistory = history
    },
    ADD_ANALYSIS(state, analysis) {
      state.analysisHistory.unshift(analysis)
    },
    SET_LOADING(state, loading) {
      state.loading = loading
    },
    SET_ERROR(state, error) {
      state.error = error
    },
    CLEAR_ERROR(state) {
      state.error = null
    }
  },
  actions: {
    login({ commit }, { user, token }) {
      commit('SET_USER', user)
      commit('SET_TOKEN', token)
    },
    logout({ commit }) {
      commit('SET_USER', null)
      commit('SET_TOKEN', null)
      commit('SET_ANALYSIS_HISTORY', [])
    },
    setAnalysisHistory({ commit }, history) {
      commit('SET_ANALYSIS_HISTORY', history)
    },
    addAnalysis({ commit }, analysis) {
      commit('ADD_ANALYSIS', analysis)
    },
    setLoading({ commit }, loading) {
      commit('SET_LOADING', loading)
    },
    setError({ commit }, error) {
      commit('SET_ERROR', error)
    },
    clearError({ commit }) {
      commit('CLEAR_ERROR')
    }
  }
})

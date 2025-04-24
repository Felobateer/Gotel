import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        userToken: null,
        userId: null,
        tokenExpiration: null,
    },
    mutations: {
        setUser(state, { token, userId }) {
            state.userToken = token;
            state.userId = userId;
            state.tokenExpiration = Date.now() + 3600 * 1000; 
        },
        clearUser(state) {
            state.userToken = null;
            state.userId = null;
            state.tokenExpiration = null;
        },
    },
    actions: {
        saveUserSession({ commit }, { token, userId }) {
            commit('setUser', { token, userId });
            localStorage.setItem('userToken', token);
            localStorage.setItem('userId', userId);
            localStorage.setItem('tokenExpiration', Date.now() + 3600 * 1000);
        },
        loadUserSession({ commit }) {
            const token = localStorage.getItem('userToken');
            const userId = localStorage.getItem('userId');
            const tokenExpiration = localStorage.getItem('tokenExpiration');

            if (token && userId && tokenExpiration && Date.now() < tokenExpiration) {
                commit('setUser', { token, userId });
            } else {
                commit('clearUser');
                localStorage.clear();
            }
        },
        clearUserSession({ commit }) {
            commit('clearUser');
            localStorage.clear();
        },
    },
    getters: {
        isAuthenticated: (state) => !!state.userToken && Date.now() < state.tokenExpiration,
        getUserToken: (state) => state.userToken,
        getUserId: (state) => state.userId,
    },
});
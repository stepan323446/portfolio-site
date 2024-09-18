import axios from 'axios';
import { createStore } from 'vuex'

export default createStore({
  state: {
    documentLocked: false,
    contacts_data: [ ],
    isLoadingContent: false
  },
  getters: {
    contacts: state => state.contacts_data,
    loadingContent: state => state.isLoadingContent
  },
  mutations: {
    documentLockOverflow(state, value) {
      state.documentLocked = value;

      if (state.documentLocked) {
        document.body.style.overflow = 'hidden';
      }
      else {
        document.body.style.overflow = 'initial';
      }
    },
    setContacts(state, contacts) {
      state.contacts_data = contacts;
    },
    setLoadingStatus(state, isLoading) {
      state.isLoadingContent = isLoading;
    }
  },
  actions: {
    fetchContacts({ commit }) {
      axios.get('/api/v1/bio/contacts').then((response) => {
        commit('setContacts', response.data)
      });
    }
  },
  modules: {
  }
})

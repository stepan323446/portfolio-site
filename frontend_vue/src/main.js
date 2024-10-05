import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import components from '@/components/UI/index'
import axios from 'axios'

import VueHighlightJS from 'vue3-highlightjs'

axios.defaults.baseURL = 'http://127.0.0.1:8000';

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
});

app
    .use(router, axios)
    .use(store)
    .use(VueHighlightJS)
    .mount('#app')

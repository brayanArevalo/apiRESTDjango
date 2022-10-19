import '@babel/polyfill'
import 'mutationobserver-shim'
//import './plugins/bootstrap-vue'
import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/bootstrap.min.css'
import '@/assets/bootstrap.bundle.min.js'
//import BootstrapVue from 'bootstrap-vue'

createApp(App).use(store).use(router).mount('#app')
//Vue.use(BootstrapVue);

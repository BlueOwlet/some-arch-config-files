import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'


// axios.defaults.baseURL='http://192.168.1.100:8000'
//axios.defaults.baseURL='http://interactspeakingcenter:8000'
//axios.defaults.baseURL='http://localhost:8000'
axios.defaults.baseURL='/api'


const app=createApp(App)



app.use(store).use(router,axios).mount('#app')

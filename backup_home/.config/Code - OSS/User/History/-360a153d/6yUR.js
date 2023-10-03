import { createStore } from 'vuex'
import axios from 'axios'
import {useRouter} from 'vue-router'
// import Websocket from 'ws'


export default createStore({
  state: {
    token:'',
    isAuthenticated:false,
    user:null,
    errors:null,
    // ws: new WebSocket('ws://192.168.1.100:8000/ws/'),

  },

  mutations: {
    initializeStore(state){
      if(localStorage.getItem('token')){
        console.log('token is present');
        state.token=localStorage.getItem('token')
        state.user=JSON.parse(localStorage.getItem('user'))
        state.isAuthenticated=true
        axios.defaults.headers.common['Authorization'] = 'Token '+state.token
        console.log(axios.defaults.headers.common['Authorization'])
      }else{
        state.token=''
        state.user=null

        state.isAuthenticated=false

        localStorage.removeItem('token')
        localStorage.removeItem('user')
        axios.defaults.headers.common['Authorization'] = ''

      }
    },

    async setAuth(state,data){

      console.log('s4etting auth');
      state.token=data.token
      state.user=data.user
      state.isAuthenticated=true
      localStorage.setItem('token',state.token)
      localStorage.setItem('user',JSON.stringify(state.user))
      axios.defaults.headers.common['Authorization'] = 'Token '+state.token


    },

    removeAuth(state){
      state.isAuthenticated=false
      state.user=null
      
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      axios.defaults.headers.common['Authorization'] = ''


    },





  },
  actions: {

      get_introduction(context,data){
        let material=data.material
        let introduction=data.introduction

        introduction.value.level=material.value.level
        introduction.value.duration=material.value.duration
        





      },

    },


    modules: {
    }
  })

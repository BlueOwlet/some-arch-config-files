<template>

  <!-- <span class="navigate" @click.stop=toggleNavBar>
    <img :src="logo">


  </span> -->

  
  
  <nav @click="toggleNavBar" :class="{show:toggle}">
    <img @click.stop="toggleNavBar" class="navigate" :src="logo" :class="{move:toggle}">

    <router-link to="/">Home</router-link>


    <template v-if="['Admin'].includes(role)">
      <router-link to="/database">DB</router-link>
      <router-link to="/admin-dashboard">Dashboard</router-link>
      
    </template>
    
    <template v-if="['Instructor'].includes(role)">
      <router-link to="/instructor-dashboard">Instructor Dashboard</router-link>
      <router-link to="/hoursheet">Hoursheet</router-link>
      
    </template>

    <template v-if="['Student'].includes(role)">
      <router-link to="/student-dashboard">Student Dashboard</router-link>
    
    </template>
    
    



    <!-- <router-link to="/signup">Sign Up</router-link> -->
    


    <router-link to="/login">Login</router-link>

    <router-link to="/logout">Logout</router-link>
  
    <!-- <router-link to="/about">About</router-link> -->
  
  </nav>

</template>


<script setup>
  import {ref} from 'vue'
  import {useStore} from 'vuex'
  let toggle=ref(false)

  let logo=ref()

  logo.value=require('@/assets/logo.png')
  let store=useStore()
  let user=store.state.user
  let role=ref(null)
  function toggleNavBar(){
    user=store.state.user
    if (user==null){
      role.value=null
    }else{
      role.value=user.role
    }
    toggle.value=!toggle.value

  }

</script>



<style scoped>

  .navigate{
    position:fixed;
    top: 0rem;
    left: 0rem;
    height:3rem;
    width:3rem;
    background:var(--blue1);
    opacity:0.8;
    border-radius:50%;
    border: 5px solid var(--white1);
    z-index:100;
    cursor:pointer;
  }

  .navigate:hover{
    opacity:1;
  }


  .move{
    position:static;
    /* left:3rem; */
    /* top:0rem */
  }

  .show{
    left:0;
  }

  nav{
    position: fixed;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    top: 0;
    left: 120%;
    height: 100vh;
    width: 20rem;
    background: var(--red1);
    color: var(--white1);
    transition: all 0.5s linear;
    font-size:x-large;
    gap:2rem;
    text-align:center;
    overflow: auto;
    z-index: 100;
  }
  a{
    display: flex;
    width: 100%;
    height: 50%;
    background: var(--blue2);
    color: var(--white1);
    justify-content: center;
    align-items: center;
    font-family: var(--passion);

  }

  a:hover{
    background: var(--black)
  }
</style>

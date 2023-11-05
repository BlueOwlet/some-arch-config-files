<template>
  <ErrorAlerts/>
  <!-- <Header/> -->
  <NavBar/>
  <router-view/>
</template>


<script setup>
  import axios from 'axios'
  import {createApp,ref,onBeforeMount} from 'vue'
  import {useStore} from 'vuex'
  import NavBar from '@/components/NavBar.vue'
  import ErrorAlerts from '@/components/ErrorAlerts.vue'
  import Header from '@/components/HeaderComponent.vue'

  import { useRouter } from 'vue-router'
  import VueGtag from 'vue-gtag';


  onBeforeMount( ()=>{
    console.log('before mounting everything once');
    let store = useStore()
    store.commit('initializeStore')


    }
  )

  const router = useRouter();

  const app = createApp();

// Initialize the gtag plugin
  app.use(VueGtag, {
    config: {
      id: 'G-S8H5RKPEH5', // Replace with your actual Google Analytics Measurement ID
    },
  }, router);


</script>

<style media="screen">

  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Passion+One&family=Satisfy&family=Ubuntu+Condensed&display=swap');




  *{

    
    
    margin: 0;
    padding: 0;
    
    
    --bebas: 'Bebas Neue', sans-serif;
    --passion: 'Passion One', cursive;
    --satisfy: 'Satisfy', cursive;
    --ubuntu: 'Ubuntu Condensed', sans-serif;
    
    font-family:var(--ubuntu);


    --shadow:var(--black) 5px 5px 2px;
    
/* ######################################### NEW SCHEME #########################################3 */

    --blue1: #253C59;
    --blue2: #2D4B73;
    --blue3: #06739e;
    
    --yellow1: #b89215;
    --yellow2: #e5c14bff;
    --yellow3: #f7c608ff;
    --yellow4: #ffd753ff;
    
    --red1: #9b3138;
    --red2: #c75058;
    --red3: #c42c52;
    
    --white1: #ece3db;
    --white2:#ffdddd;
    --black: #36363f;
    --gray:rgb(133, 133, 133);
    --gray1: #8697A6;

    --green:#30b195;
    --green1:#30b195;
    --green2:#40bfa4;




/* ######################################### ANIMATIONS #########################################3 */

    --home:2s;









/* ######################################### OLD SCHEME #########################################3 */

    --database: rgb(74, 132, 165);
    --primary:rgb(21, 89, 179);
    --secondary:rgb(206, 206, 206);
    --options:rgb(163, 7, 7);
    --selected:rgb(141, 40, 79);
    --border:black;
    --box-shadow:black;

    --title: 2rem;




    --section:rgb(13, 81, 138);
    --group: rgb(255, 255, 255);


    --group-color: rgb(163, 24, 85);
    --group-color-dark:rgb(116, 8, 55);

    --confirmation-dark:rgb(80, 80, 80);
    --confirmation: white;
    
    --transition:0.4s all linear;


  }
  html{
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
    background:var(--white);
  }

  a {
    color: inherit;
    text-decoration: none;
  }


</style>

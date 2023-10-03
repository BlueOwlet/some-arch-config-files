<template>

  <NavBar/>



  <router-view/>

  <Footer/>
</template>


<script setup>
  import NavBar from "@/components/NavBar.vue"
  import Footer from "@/components/Footer.vue"


</script>

<style>


  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Passion+One&family=Satisfy&family=Ubuntu+Condensed&display=swap');
  


  html{

    /* FONTS */
    --bebas: 'Bebas Neue', sans-serif;
    --passion: 'Passion One', cursive;
    --satisfy: 'Satisfy', cursive;
    --ubuntu: 'Ubuntu Condensed', sans-serif;

    font-family:var(--ubuntu);
    
    
    
    /* THEME */
    --primary:#66CC99;
    --accent: #66CC99;
    
    --background: #f4f4f4;
    --shadow: #434343;

    --white: #f4f4f4;
    --dark: #434343;

    --gradient: linear-gradient(135deg, #66CC99, #0099CC);

    /* OPTIONS */
    --rounded: 5px;
    --shadowed: 0px 0px 10px 0px var(--shadow);

    color: var(--dark);


    /* TRANSITIONS */
    --transition: all 0.1s ease-in;

    margin:0;
    padding:0;
    background: var(--white);







  }







  .title{
    font-size: 60px;
    text-align: center;

  }


  button {
    width: fit-content;
    background: var(--white);
    transition: var(--transition);
    border-radius:var(--rounded);
    box-shadow: var(--shadowed);
    padding:0.5rem;
    font-size:larger;
    

  }
  button:hover{
    background: var(--primary);
    color:var(--white);
  }

  button:active{
    background: var(--dark);
  }



</style>

<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>


  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Passion+One&family=Satisfy&family=Ubuntu+Condensed&display=swap');
  
  
  #app{
    margin:0;
    padding:0;


    margin: 0;
    padding: 0;


    --bebas: 'Bebas Neue', sans-serif;
    --passion: 'Passion One', cursive;
    --satisfy: 'Satisfy', cursive;
    --ubuntu: 'Ubuntu Condensed', sans-serif;

    font-family:var(--ubuntu);

    --accent: #66CC99;
    --background: #f4f4f4;
    --gradient: linear-gradient(135deg, #66CC99, #0099CC);

  }



</style>

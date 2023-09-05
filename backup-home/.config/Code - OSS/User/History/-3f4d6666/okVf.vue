<template>
  <div class="header">
    <div class="title">
      Vyda.mx
    </div>
    <div class="motto">
      Your Space, Your Community, Your Vyda
    </div>
    <div class="login">
      <input class="username" placeholder="username">
      <input class="password" type="password" placeholder="password">
      <button class="button"> Login </button>
    </div>
  </div>

</template>

<script setup>

</script>

<style>
  .header{
    width: 100%;
    background: var(--primary);
    display: grid;
    grid-template-areas: 
                        ". title login"
                        ". motto login";

    justify-content: space-between;
    align-items: center;
  }



  .title{
    grid-area: title;
  }

  .motto{
    font-size: large;
    grid-area: motto;
  }


  .login{
    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;
    background: var(--background);
    grid-area: login;
  }



</style>

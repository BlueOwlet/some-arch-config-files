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

  <div class="plans">
    <div class="plan">
      PLAN MENSUAL
    </div>
    <div class="plan">
      PLAN ANUAL
    </div>
  </div>

</template>

<script setup>

</script>

<style>
  .header{
    width: 100%;
    height: 30vh;
    background: var(--primary);
    display: grid;
    grid-template-areas: 
                        ". title login"
                        ". motto login";

    justify-content: space-evenly;
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
    padding: 1rem;
    justify-content: center;
    align-items: center;
    background: var(--background);
    grid-area: login;
    border-radius: var(--rounded);
    box-shadow: var(--shadowed);
    gap: 1rem;
  }




  .plans{
    display: flex;
    justify-content: space-evenly;
    margin-top: 1rem;
  }

  .plan{
    background: var(--primary);
    color: var(--white);
    border-radius: var(--rounded);
    box-shadow: var(--shadowed);
    font-size: x-large;
    padding: 2rem;
    
  }


</style>

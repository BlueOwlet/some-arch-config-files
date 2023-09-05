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
                        ". title login" 100%;
  }



  .motto{
    font-size: large;
  }



</style>

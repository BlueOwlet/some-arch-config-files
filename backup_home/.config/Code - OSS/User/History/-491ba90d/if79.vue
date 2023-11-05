<template lang="html">

  <div class="card">

    <span class='total'>{{ object.total }}</span>
    <span class="title">{{object.title}}</span>


  </div>

</template>

<script setup>
  import axios from 'axios'
  import {ref} from 'vue'

  let object=ref()





  defineExpose({

    object

  })


















</script>

<style lang="css" scoped>
  .card{
    display: flex;
    flex-direction: column;
    background: var(--red3);
    color:var(--white1);
    height: 10rem;
    width: 15rem;
    align-items:end;
    justify-content:center;
    border-radius: 1rem;
  }

  .total{
    font-weight: bold;
    font-size: xxx-large;
  }

  .title{
    font-size: xx-large;
  }

  .student{
    background: var(--blue1);
  }
  .instructor{
    background: var(--red1);
  }
  .group{
    background:var(--yellow1);
  }
















</style>

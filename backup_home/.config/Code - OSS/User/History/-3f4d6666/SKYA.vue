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

  <div class="key-features">
    <div class="key-feature" v-for="key_feature in data.key_features">
       <div class="key-feature-title">
        {{ key_feature.title }}
       </div>
       <div class="key-feature-description">
        {{key_feature.description}}
       </div>
    </div>
  </div>

</template>

<script setup>
  import {ref, reactive, onMounted, onBeforeMount} from 'vue'
  let data=reactive({})
  data.key_features=[
    {
      title:'Reuniones Sin Limite de Tiempo',
      description:`
      Conversaciones prolongadas sin preocuparte por tiempo.
      `
  },
    {
      title:'Seguridad y Privacidad',
      description:`
      Protegemos datos y comunicaciones para garantizar privacidad.
      `
    },
    {
      title:'Calidad de Video y Audio',
      description:`
      Experiencia nítida y audio claro en videoconferencias. 
      `
    },
    {
      title:'Facilidad de Uso y Accesibilidad',
      description:`
      Plataforma intuitiva para unirse a conferencias sin problemas.
      `
    },
    {
      title:'Grabacion de Conferencias',
      description:`
      Graba videoconferencias para revisarlas o compartirlas.
      `

    },


  ]

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
    align-self: start;
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
    font-size: larger;
    padding: 1rem;
    
  }




  .key-features{
    display: flex;
    justify-content: center;
    gap:10px;
    padding-top: 2rem;
  }
  
  .key-feature{
    background: var(--gradient);
    border-radius: var(--rounded);
    box-shadow: var(--shadowed);
    padding: 1rem;
    color: var(--white);

    width:200px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    text-justify: center;
  }

  .key-feature-title{
    font-size: xx-large;

  }

  .key-feature-description{
    font-size: large;

  }


</style>

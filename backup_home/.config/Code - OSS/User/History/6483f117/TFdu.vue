<template>
  <div class="header">
    <div class="title">
      Vyda.mx
    </div>
    <div class="motto">
      Tu Espacio, Tu Comunidad, Tu Vyda
    </div>
    <div class="login">
      <input class="username" placeholder="username">
      <input class="password" type="password" placeholder="password">
      <button class="button"> Login </button>
    </div>
  </div>

  <div class="plans">
    <div class="plan">
      <div>
        PLAN MENSUAL 
      </div>
      <div>
        199 MXN.-
      </div>
    </div>
    <div class="plan">
      <div>
        PLAN ANUAL 
      </div>
      <div>
        1,799 MXN.-
      </div>
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

  <div class="main-product-image">
    <img src="@/assets/main-product.png">
  </div>

</template>

<script setup>
  import {ref, reactive, onMounted, onBeforeMount} from 'vue'
  import axios from 'axios'
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


  onBeforeMount(()=>{
    let response=axios.post('/test/test1')
    console.log(response.data)
  })



</script>

<style>
  .header{
    width: 100%;
    height: 30vh;
    background: var(--gradient);
    display: grid;
    grid-template-areas: 
                        ". title login"
                        ". motto login";

    justify-content: space-evenly;
    align-items: center;
    transition: var(--transition);
  }


  @media screen {
    
  }

  @media (max-width:1000px){

    .header{
      height: 100vh;
      grid-template-areas: 
                          "title"
                          "motto"
                          "login";

    }

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
    padding-top: 3rem;

  }

  .plan{
    background: var(--gradient);
    color: var(--white);
    border-radius: var(--rounded);
    box-shadow: var(--shadowed);
    font-size: larger;
    padding: 1rem;
    text-align: center;
    
  }




  .key-features{
    display: grid;
    justify-content: center;
    gap: 1rem;
    padding-top: 3rem;
    grid-template-columns: repeat(auto-fit, 230px);
  }

  
  .key-feature{
    background: var(--gradient);
    border-radius: var(--rounded);
    box-shadow: var(--shadowed);
    padding: 5px;
    color: var(--white);

    width:200px;
    height: 250px;

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    text-align: center;
    text-justify: center;
  }

  .key-feature-title{
    font-size: xx-large;

  }

  .key-feature-description{
    font-size: large;
    justify-self: start;

  }

  .main-product-image{
    width: 100%;
    height: auto;
  }

  .main-product-image img{
    width: 100%;
    height: auto;
  }


</style>

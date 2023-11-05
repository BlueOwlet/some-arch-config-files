<template>


<div class="section cards">
    <Card ref="students"/>  
    <Card ref="instructors"/>  
    <Card ref="groups"/>  
    <router-link to="/bad-attendances">
      <Card ref="bad_attendances"/>  
    </router-link>





  </div>



  <div class="section">
    <Instructors/>
  </div>

  <div class="section">
    <AdminMaker/>
  </div>



  <!-- <div class="section">
    <Collections/>
  </div> -->


    
  <div class="section">

    <InitialMessage/>
  </div>
    


<router-link to="/database">Database</router-link>



</template>

<script setup>
  import {ref, onBeforeMount, reactive} from 'vue'
  import axios from 'axios'
  import Card from '@/components/DashboardCard.vue'

  import AdminMaker from '@/components/AdminMaker.vue'

  import Instructors from '@/components/Instructors.vue'

  import InitialMessage from '@/components/InitialMessage.vue'

  import Collections from '@/components/Collections.vue'


    let students=ref()
    let instructors=ref()
    let groups=ref()
    let bad_attendances=ref()

    let collection=reactive({})


  onBeforeMount(async()=>{
    let response=await axios.post('/dashboard/get_objects/')
    let data=response.data
    
    students.value.object={
                                title:'Students',
                                total:data.students

                              }

    instructors.value.object={
                                title:'Instructors',
                                total:data.instructors

                              }

    groups.value.object={
                                title:'Groups',
                                total:data.groups

                              }

    bad_attendances.value.object={
                                title:'Bad Attendances',
                                total:data.bad_attendances

                              }
    


    
      

  })
  



</script>



<style scoped>

  .cards{
    display: grid;
    grid-template-columns: repeat(auto-fill,20rem);
    gap: 1rem;
    justify-items: center;
    justify-content: center;
    align-items: center;
    width: 100vw;
    background:var(--white1);
  }


  .section{
    width:100vw;
    background:var(--blue1);

  }

  .section:nth-child(2n){
    background:var(--red1)
  }



</style>
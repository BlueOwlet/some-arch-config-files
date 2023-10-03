<template>

    <div @click="show_navbar()" class="navbarlogo">
        <img src="@/assets/logo.png">
    </div>

    <nav class="navbar" :class="{show:data.shownavbar}">
        <router-link to="/">Home</router-link>
        <router-link to="/">Login</router-link>
    </nav>


</template>



<script setup>
    import {reactive,ref,onMounted,onBeforeMounted} from 'vue'

    let data=reactive({})

    data.shownavbar=false

    function show_navbar(){
        data.shownavbar=!data.shownavbar
    }



</script>



<style scoped>

    .navbar{
        position: absolute;
        top:0;
        height: 0;
        width: 0;
        background: var(--dark);
        display: flex;
        justify-content:space-evenly;
        align-items:center;
        /* z-index: -100; */
        opacity: 0;
        transition: all 0.5 linear;



    }

    .navbarlogo{
        position: absolute;
        z-index:100;
    }

    .show{
        /* z-index: 90; */
        opacity:1;
        height: 100vh;
        width: 100%;

    }




    a {
        background: var(--gradient);
        border-radius: var(--rounded);
        box-shadow: var(--shadowed);

    }

    a:hover {
        background: var(--primary);
    }


</style>
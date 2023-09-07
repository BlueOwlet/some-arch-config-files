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


    .navbarlogo{
        position: fixed;
        z-index:100;
        width: 7rem;
        height: 7rem;
        background:var(--dark);
        border-radius: 50%;
        display: flex;
        align-items:center;
        justify-content:center
    }
    .navbarlogo img{
        width:90%;
        height: auto;
    }

    .navbar{
        z-index:-100;
        position: fixed;
        top:50%;
        left:50%;
        transform:translate(-50%,-50%);
        height: 0;
        width: 0;
        border-radius:50%;
        background: var(--dark);
        display: flex;
        flex-direction: column;
        justify-content:space-evenly;
        align-items:center;
        /* z-index: -100; */
        opacity: 0;
        transition: var(--transition);
        opacity: 0;



    }


    .show{
        z-index: 90;
        opacity:1;
        height: 100vh;
        width: 100%;
        border-radius: 0%;
        background:var(--gradient);
        opacity: 1;

    }




    a {
        font-size: xx-large;
        border-radius: var(--rounded);
        box-shadow: var(--shadowed);
        color: var(--dark);
        font-family:var(--passion);
        transition: var(--transition);
        padding:1rem;

    }

    a:hover {
        transform: scale(1.3);
    }


</style>
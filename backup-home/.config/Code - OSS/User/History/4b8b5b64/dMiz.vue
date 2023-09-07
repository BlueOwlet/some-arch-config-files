<template>

    <div class="navbarlogo">
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

    data.shownavbar=true


</script>



<style scoped>

    .navbar{
        position: sticky;
        top: -100%;
        height: 0;
        width: 0;
        background: var(--dark);
        display: flex;
        justify-content:space-evenly;
        align-items:center;
        z-index: -100;
        opacity: 0;



    }

    .navbarlogo{
        position: absolute;
        z-index:100;
    }

    .show{
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
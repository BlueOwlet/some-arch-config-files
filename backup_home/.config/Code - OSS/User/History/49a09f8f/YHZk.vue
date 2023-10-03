<template>
    <div class="footer">
    
        © 2023 Vyda.mx. All rights reserved.

    </div>

</template>



<script setup>
    import {reactive,ref,onMounted,onBeforeMounted} from 'vue'

    let data=reactive({})


</script>



<style scoped>

    .footer{
        width: 100%;
        height: 20vh;
        background: var(--dark);
        color: var(--white);
        display:flex;
        justify-content:center;
        align-items:center;
        text-align:center;
        text-justify:center
    }

</style>
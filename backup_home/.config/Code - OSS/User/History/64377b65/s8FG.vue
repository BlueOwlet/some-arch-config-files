<template>
    <table class="instructors">
        <thead>
            <th>Instructor</th>
            <th>Dashboard</th>
            <th>Hoursheet</th>

        </thead>
        <tbody>
            <tr class="instructor" v-for="instructor in data.instructors">
                <td>
                    {{instructor.ui}}                    
                </td>
                <td>
                    <a :href="'/instructor-dashboard?user_id='+instructor.user">
                        dashboard
                    </a>
                </td>
                <td>
                    <a :href="'/hoursheet?user_id='+instructor.user">
                        hoursheet
                    </a>
                </td>
            </tr>
        </tbody>

    </table>



</template>


import LoginViewVue from '@/views/LoginView.vue'
<script setup>
    import {ref,reactive,onMounted,onBeforeMount} from 'vue'
    import axios from 'axios'
    let data=reactive({})

    onBeforeMount(async()=>{
        
        let response=await axios.post('/adminmaker/get_instructors/')
        console.log(response.data)
        data.instructors=response.data
    })



</script>



<style scoped>
    .instructors{
        width: 100%;
        text-align: center;
        border-collapse: collapse;



    }

    .instructor{
        font-size:xxx-large;
        border-top:5px solid var(--white1);
        border-bottom:5px solid var(--white1);
        color:var(--white1);

    }


</style>
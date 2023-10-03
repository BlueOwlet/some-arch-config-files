<template>
    <div class="container">
        <div class="students">
            <div class="active-student" v-if="data.students.active" v-for="student in data.students.active">
                <div>
                    {{ student.ui }} 
                </div>
                <div @click.stop="get_payments(student)" class="last-payments">
                    <div class="last-payment" :class="{paid:last_payment.paid}" v-for="last_payment in student.last_payments">
                        {{ last_payment.ui }}
                    </div>
                </div>  
            </div>
            <div class="inactive-student" v-if="data.students.inactive" v-for="student in data.students.inactive">
                <div>
                    {{ student.ui }}
                </div>
                <div @click.stop="get_payments(student)" class="last-payments">
                    <div class="last-payment"  :class="{paid:last_payment.paid}" v-for="last_payment in student.last_payments">
                        {{ last_payment.ui }}
                    </div>
                </div>  
            </div>

        </div>
        

    </div>


    <Payments/>

</template>

<script setup>
    import {reactive,ref,onMounted,onBeforeMount,provide} from 'vue'
    import axios from 'axios'

    import Payments from '@/components/Payments.vue'

    let data=reactive({
        students:{
            active:{},
            inactive:{},
        },
        payments_show:false,
    })


    provide('data',data)
    // provide('payments_show',data.payments_show)



    onBeforeMount(async ()=>{
        let response=await axios.post('/adminmaker/get_students/')

        data.students=response.data

    })


    // async function get_payments(student){
    //     let response=await axios.post('/adminmaker/get_payments/',{student_id:student.id})

    //     data.payments=response.data
    //     data.payments_fullscreen=true
    //     data.student=student
    //     console.log(data)
    // }


    async function get_payments(student){
        let response=await axios.post('/manager/get_payments/',{student_id:student.id})

        data.payments=response.data
        data.payments_fullscreen=true
        data.student=student
        console.log(data)
    }



</script>




<style scoped>

    .container{

        width:100vw;
        

    }

    .students{
        display:grid;
        grid-template-columns:repeat(auto-fill,10rem);
        justify-content:center;
        justify-items:center;
        align-items:center;

    }

    .active-student{
        border-radius:1rem;
        border: 5px solid var(--green1);
        background:var(--blue1);
        color:var(--white1);


    }

    .inactive-student{
        border-radius:1rem;
        border: 5px solid var(--red2);
        background:var(--blue1);
        color:var(--white1);
    }


    .last-payments{
        display: flex;
        flex-direction: column;
        justify-content:center;
        justify-items:center;
        align-items:center;
        padding: 1rem;
    }


    .last-payment{
        background:var(--red2);
    }

    .paid{
        background:var(--green1);
    }

</style>
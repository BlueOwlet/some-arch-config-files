<template>

    <div class="container">

        <div class="timing">
            <input v-model="initial_datetime" type="datetime-local">
            <input v-model="final_datetime" type="datetime-local">
            <button @click.stop="filter">Filter</button>
        </div>
        <div @click.stop="reset" class="bad-attendances">
            <div class="bad-attendance" v-for="attendance in data.bad_attendances">
                <div class="attendance-admin-check">
                    Admin Check: {{ attendance.admin_check }}
                </div>
                <div class="attendance-group">
                    <template v-if="attendance.group">
                        {{ attendance.group.subject }} | 
                        <template v-for="instructor in attendance.group.instructor">
                            {{ instructor.ui }}. 
                        </template>
                    </template>
                </div>
                <div class="attendance-datetime">
                    {{ attendance.datetime }}
                </div>

                <template v-if="attendance.instructor_confirmation.length!=0">
                    <div class="instructor-confirmation">
                        {{ attendance.instructor_confirmation.at(-1).ui }}
                    </div>
                </template>
                <template v-else>
                    <div class="instructor-confirmation">
                        Instructor did not confirm
                    </div>
                </template>
                <div  class="student-confirmations">
                    <template v-for="student_confimation in attendance.student_confirmations">
                        <div @click.stop="get_student_payments(student_confimation.student,attendance)">
                            {{ student_confimation.ui }}
                        </div>
                    </template>
                </div>
            </div>
        </div>
    </div>


    <Payments/>

    
    
    
</template>


<script setup>
    import axios from 'axios'
    import Payments from '@/components/Payments.vue'
    import {ref,reactive, onBeforeMount, provide} from 'vue'


    let bad_attendances=reactive({})

    let data=reactive({})


    let datetime=new Date()
    let initial_datetime=ref(datetime.getFullYear(),datetime.getMonth(),datetime.getDate())
    let final_datetime=ref(datetime.getFullYear(),datetime.getMonth(),datetime.getDate())

    provide('data',data)



    async function filter(){
        let response=await axios.post('/dashboard/filtered_bad_attendances/',{initial_datetime:initial_datetime.value,final_datetime:final_datetime.value})

        data.bad_attendances=response.data
        fix_bad_attendances()

    }


    onBeforeMount(async ()=>{
        let response = await axios.post('/dashboard/bad_attendances/')
        data.bad_attendances=response.data
        fix_bad_attendances()


    })


    function fix_bad_attendances(){
        

        data.bad_attendances.forEach(attendance=>{
            attendance.student_confirmations=[]
            if(!attendance.group){
                return
            }
            attendance.group.student.forEach(student=>{

                let actual_student_confirmations=attendance.student_confirmation.filter(confirmation=>{
                    return confirmation.student==student.id
                })

                let actual_student_confirmation=actual_student_confirmations.at(-1)
                if(!actual_student_confirmation){
                    actual_student_confirmation={}
                    actual_student_confirmation.ui=student.ui + ' did not confirmed'
                }
                actual_student_confirmation.student=student
                attendance.student_confirmations.push(actual_student_confirmation)
            })

        })
        
        
    }

    async function get_student_payments(student,attendance){
        let response=await axios.post('/adminmaker/get_payments/',{student_id:student.id})
        data.payments=response.data
        data.attendance=attendance
        data.student=student
        data.payments_fullscreen=true

    }


</script>



<style scoped>

    .container{
        width: 100vw;
        background: var(--gray);
        display: grid;
        gap:1rem;
        justify-content: center;
        justify-items:center;
        align-items: center;



    }

    .bad-attendances{
        display: grid;
        grid-template-columns: repeat(auto-fill,10rem);
        width: 90vw;
        background: var(--gray);
        gap:1rem;
        justify-content:center;
        align-items: center;


    }

    .bad-attendance{

        background: var(--red1);
        color:var(--white1);
        border-radius: 1rem;
        border: 5px solid var(--red3);
        padding:1rem;

        gap:1rem;




        display: grid;
        grid-template-areas:
                    'group'
                    'datetime'
                    'instructor-confirmation' 
                    'student-confirmations';
    }

    .attendance-datetime{
        grid-area: datetime;
    }

    .attendance-group{
        grid-area: group;
    }

    .instructor-confirmation{
        grid-area: instructor-confirmation;
    }
    .student-confirmations{
        grid-area: student-confirmations;
        display: flex;
        flex-direction: column;
    }


</style>
<template>





    <div @click.stop="close" class="container-payments" :class="{fullscreen:data.payments_fullscreen}">


        <template v-if="data.attendance">

            <div @click.stop class="bad-attendance">


                <select @change.stop="update_attendance_package($event,data.attendance,null,null)">
                    <option value="" selected></option>
                    <template v-for="(payment, payment_index) in data.payments">
                        <template v-for="(package_0, package_index) in payment.package">
                            <option :value="package_0"> Payment: {{ Object.keys(data.payments).length - payment_index}} | Package: {{ Object.keys(payment.package).length - package_index }}</option>
                        </template> 
                    </template>
                </select>                

                <input @change.stop="update_attendance(data.attendance)" type="datetime-local" v-model="data.attendance.datetime">
                <input @change.stop="update_attendance(data.attendance)" v-model="data.attendance.duration" type="number" min="0" max="24">
                
                <div class="instructor-confirmations">
                    <div class="instructor-confirmations-title">
                        Instructor Confirmation(s):
                        <button @click.stop="create_instructor_confirmation(data.attendance)" class="add">+</button>
                    </div>
                    <template v-for="instructor_confirmation in data.attendance.instructor_confirmation">
                        <div class="instructor-confirmation">
                            <label class="instructor-confirmation-title" v-if="instructor_confirmation">
                                {{ instructor_confirmation.instructor.ui }} Confirmation:
                            </label>
                            <div confirmation>
                                <select @change.stop="update_instructor_confirmation(instructor_confirmation)" v-model="instructor_confirmation.confirmation">
                                    <option :value="option" v-for="option in confirmation_options">{{ option }}</option>
                                    <option :value="instructor_confirmation.confirmation">{{ instructor_confirmation.confirmation }}</option>
                                </select>
                            </div>

                            <button @click.stop="delete_instructor_confirmation(instructor_confirmation,data.attendance)" class="delete">-</button>

                        </div>
                        
                    </template>
                </div>
                <div class="student-confirmations">
                    <div class="student-confirmations-title">
                        Student Confirmation(s):
                        <button @click.stop="create_student_confirmation(data.attendance)" class="add">+</button>
                    </div>
                    <template v-for="student_confirmation in data.attendance.student_confirmation">
                        <div class="student-confirmation">
                            <label class="student-confirmation-title" v-if="student_confirmation">
                                {{ student_confirmation.student.ui }}:
                            </label>
                            <div class="confirmation">
                                <select @change.stop="update_student_confirmation(student_confirmation)" v-model="student_confirmation.confirmation">
                                    <option :value="option" v-for="option in confirmation_options">{{ option }}</option>
                                    <option :value="student_confirmation.confirmation">{{ student_confirmation.confirmation }}</option>
                                </select>
                            </div>
                            <button @click.stop="delete_student_confirmation(student_confirmation,data.attendance)" class="delete">-</button>
                        </div>

                    </template>
                </div>

                <div>
                    <input v-model="data.attendance.link">
                </div>

                <div>
                    <button @click.stop="delete_attendance(data.attendance)" class="delete">-</button>
                </div>

            </div>

        </template>












        <a @click.stop :href="'/student-dashboard?user_id=' + data.student.user.id">
            <div  class="title">
                {{ data.student.ui }}
            </div>
            <template v-if="data.attendance">
                <div v-if="data.attendance.group">
    
                    {{ data.attendance.group.schedule }}
                </div>
            </template>
        </a>

        <button class="make_monthly" @click.stop="all_into_one()">All attendances in one package</button>
        <button class="make_monthly" @click.stop="make_all_monthly()">Make All Monthly</button>
        <button class="make_monthly" @click.stop="fix_in_packages()">Fix in Packages</button>
        
        
        
        <label>
            Add Payment:
            <button @click.stop="create_payment()" class="add">+</button>
        </label>



        <!--    PAYMENT STARTS HERE  -->
        <div class="payment" :class="{paid:payment.paid, show_payment:payment.show}" v-if="data.payments" v-for="(payment,payment_index) in data.payments">
            <div @click.stop="show_payment(payment)" class="payment-title"> Payment: {{ Object.keys(data.payments).length-payment_index }}</div>

            <div @click.stop v-if="payment.show"> 

                <button class="make_monthly" @click.stop="default_datetimes(payment)">Default Datetimes</button>
                <button class="make_monthly" @click.stop="delete_duplicate_datetimes(payment)">Delete Duplicate Dates</button>
                <button class="make_monthly" @click.stop="make_monthly(payment)">Make monthly from here on up</button>
    
                <table class="edit-payment">
                    <thead>
                        <th>Datetime</th>
                        <th>Amount</th>
                        <th>Paymnet Method</th>
                        <th>Status</th>
                        <th>Reference</th>
                        <th>Paid</th>
                        <th>Comments</th>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <input @change.stop="update_payment(payment)" type="datetime-local" v-model="payment.datetime">
                            </td>
                            <td>
                                <input @change.stop="update_payment(payment)" type="number" step="0.01" v-model="payment.amount"> MXN
    
                            </td>
                            <td>
                                <select @change.stop="update_payment(payment)" v-model="payment.method">
                                    <option :value="option" v-for="option in payment_method_options">{{ option }}</option>
                                    <option :value="payment.method">{{ payment.method }}</option>
                                    
                                </select>
                            </td>
    
                            <td>
                                <input @change.stop="update_payment(payment)" v-model="payment.status">
    
    
                            </td>
                            <td>
                                <input @change.stop="update_payment(payment)" v-model="payment.reference">                    
    
    
                            </td>
                            <td>
                                <input @change.stop="update_payment(payment)" type="checkbox" v-model="payment.paid">
    
    
                            </td>
                            <td>
                                <textarea @change.stop="update_payment(payment)" v-model="payment.comments"></textarea>
    
    
                            </td>
                            <td>
                                <button @click.stop="delete_payment(payment)" class="delete">-</button>
    
                            </td>
                        </tr>
                    </tbody>
    
    
                </table>
                <div class="packages" @click.stop  v-if="payment.package">
    
                    <label>
                        Add Package:
                        <button @click.stop="create_package(payment)" class="add">+</button>
                    </label>
    
    
                    <div class="package" v-for="(package_,package_index) in payment.package" >
                        <div class="package-title">
                            Package: {{ Object.keys(payment.package).length - package_index}}
                        </div>
                        <table class="edit-package">
                            <thead>
                                <th>Datetime</th>
                                <th>Taken Hours</th>
                                <th>Package Hours</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        <input @change.stop="update_package(package_)" type="datetime-local" v-model="package_.datetime">
                                    </td>
                                    <td>
                                        <input @change.prevent="update_package(package_)" v-model="package_.taken_hours" type="number" min="0" max="24">
                                    </td>
                                    <td>
                                        <input @change.stop="update_package(package_)" v-model="package_.package_hours" type="number" min="0" max="24">
                                    </td>
                                    <td>
                                        <button @click.stop="delete_package(package_)" class="delete">-</button> 
                                    </td>
                                </tr>
                            </tbody>
    
                        </table>
                        <div class="attendances">
                            <label>
                                Add Attendance:
                                <button @click.stop="create_attendance(package_)" class="add">+</button>
    
                            </label>
    
                            <table>
                                <thead>
                                    <th>Package</th>
                                    <th>Datetime</th>
                                    <th>Duration</th>
                                    <th>Instructor Confirmation</th>
                                    <th>Student Confirmation</th>
                                    <th>Link</th>
                                </thead>
                                <tbody>
    
    
                                    <tr class="attendance" :id="attendance.id" v-for="attendance in package_.attendance">
                                        <td>
                                            {{ attendance.id }}
                                        </td>
    
                                        <td>
                                            <select @change.stop="update_attendance_package($event,attendance,package_,payment)" :value="package_.id">
                                                <template v-for="(payment, payment_index) in data.payments">
                                                    <template v-for="(package_0, package_index) in payment.package">
                                                        <option :value="package_0">Payment: {{ Object.keys(data.payments).length - payment_index}} | Package: {{ Object.keys(payment.package).length - package_index }}</option>
                                                    </template>
                                                </template>
                                            </select>
    
                                        </td>
                                        <td>
                                            
                                            <input @change.stop="update_attendance(attendance)" type="datetime-local" v-model="attendance.datetime">
                                        </td>
    
                                        <td>
                                            <input @change.stop="update_attendance(attendance)" v-model="attendance.duration" type="number" min="0" max="24">
    
                                        </td>
    
                                        <td>
    
                                            <div class="instructor-confirmations">
                                                <div class="instructor-confirmations-title">
    
                                                    <button @click.stop="create_instructor_confirmation(attendance)" class="add">+</button>
                                                </div>
                                                <template v-for="instructor_confirmation in attendance.instructor_confirmation">
                                                    <div class="instructor-confirmation">
                                                        <label class="instructor-confirmation-title" v-if="instructor_confirmation.instructor">
                                                            {{ instructor_confirmation.id }} {{ instructor_confirmation.instructor.ui }} Confirmation:
                                                        </label>
                                                        <div confirmation>
                                                            <select @change.stop="update_instructor_confirmation(instructor_confirmation)" v-model="instructor_confirmation.confirmation">
                                                                <option :value="option" v-for="option in confirmation_options">{{ option }}</option>
                                                                <option :value="instructor_confirmation.confirmation">{{ instructor_confirmation.confirmation }}</option>
                                                            </select>
                                                        </div>
        
                                                        <button @click.stop="delete_instructor_confirmation(instructor_confirmation,attendance)" class="delete">-</button>
        
                                                    </div>
                                                    
                                                </template>
                                            </div>
    
                                        </td>
                                        
    
                                        <td>
                                            <div class="student-confirmations">
                                                <div class="student-confirmations-title">
                                                    
                                                    <button @click.stop="create_student_confirmation(attendance)" class="add">+</button>
                                                </div>
                                                <template v-for="student_confirmation in attendance.student_confirmation">
                                                    <div class="student-confirmation">
                                                        <label class="student-confirmation-title" v-if="student_confirmation.student">
                                                                {{ student_confirmation.student.ui }}:
                                                        </label>
                                                        <div class="confirmation">
                                                            <select @change.stop="update_student_confirmation(student_confirmation)" v-model="student_confirmation.confirmation">
                                                                <option :value="option" v-for="option in confirmation_options">{{ option }}</option>
                                                                <option :value="student_confirmation.confirmation">{{ student_confirmation.confirmation }}</option>
                                                            </select>
                                                        </div>
                                                        <button @click.stop="delete_student_confirmation(student_confirmation,attendance)" class="delete">-</button>
                                                    </div>
        
                                                </template>
                                            </div>
    
                                        </td>
    
                                        <td>
                                            <div>
                                                <input v-model="attendance.link">
                                            </div>
    
                                        </td>
                                        <td>
                                            <div>
                                                <button @click.stop="delete_attendance(attendance)" class="delete">-</button>
                                            </div>
    
                                        </td>
    
                                    </tr>
    
    
    
                                </tbody>
                            </table>
    
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
    import {ref,reactive,onMounted,onBeforeMount,inject} from 'vue'
    import axios from 'axios'
    import {useRouter} from 'vue-router'
    
    let router=useRouter()

    let data=inject('data')

    let confirmation_options=ref([
        'confirmed',
        'cancelled-late',
        'cancelled-on-time',
        'no-show',
        'reschedule',
        'pending',
    
    ])

    let payment_method_options=ref([
        'DANA',
        'paypal sloth',
        'paypal owl',
        'paypal lion',
        'clip',
        'Scotia',
        'Aztec',
        'bbva',
        'mScotia',
        'iSantan',
    
        'paypal sloth @end',
        'paypal owl @end',
        'paypal lion @end',
        'clip @end',
        'Scotia @end',
        'Aztec @end',
        'bbva @end',
        'mScotia @end',
        'iSantan @end',

    ])






    function close(){
        data.student={}
        data.payments={}
        data.attendance={}
        data.payments_fullscreen=false
    }



    function assign_bad_attendance(){
        data.payments.forEach(payment=>{
            payment.package.forEach(package_=>{
                package_.attendance.forEach(attendance=>{
                    if(attendance.id == data.attendance.id){
                        data.attendance=attendance
                    }
                })
            })
        })

    }



    async function update_payment(payment){
        
        let response=await axios.post('/adminmaker/update_payment/',{payment:payment})
        Object.assign(payment, response.data);

    }   

    async function update_package(package_){
        
        let response=await axios.post('/adminmaker/update_package/',{package:package_})
        Object.assign(package_, response.data);

    }  

    async function update_attendance(attendance){
        
        let response=await axios.post('/adminmaker/update_attendance/',{attendance:attendance})
        Object.assign(attendance, response.data);
        assign_bad_attendance()

    }  

    async function update_instructor_confirmation(confirmation){
        
        let response=await axios.post('/adminmaker/update_instructor_confirmation/',{confirmation:confirmation})
        Object.assign(confirmation, response.data);
        assign_bad_attendance()
    }  
    async function update_student_confirmation(confirmation){
        
        let response=await axios.post('/adminmaker/update_student_confirmation/',{confirmation:confirmation})
        Object.assign(confirmation, response.data);
        assign_bad_attendance()
    }  


    async function create_payment(){
        let response=await axios.post('/adminmaker/create_payment/',{student_id:data.student.id})
        data.payments=response.data


    }


    async function delete_payment(payment){
        let response=await axios.post('/adminmaker/delete_payment/',{student_id:data.student.id,payment_id:payment.id})
        data.payments=response.data
    }


    async function create_package(payment){
        let response=await axios.post('/adminmaker/create_package/',{student_id:data.student.id,payment_id:payment.id})
        Object.assign(data.payments,response.data)
    }

    async function delete_package(package_){
        let response=await axios.post('/adminmaker/delete_package/',{student_id:data.student.id,package_id:package_.id})
        Object.assign(data.payments,response.data)
    }

    async function create_attendance(package_){
        let response=await axios.post('/adminmaker/create_attendance/',{student_id:data.student.id,package_id:package_.id})
        Object.assign(data.payments,response.data)
    }

    async function delete_attendance(attendance){
        let response=await axios.post('/adminmaker/delete_attendance/',{student_id:data.student.id,attendance_id:attendance.id})
        Object.assign(data.payments,response.data)
        
    }


    async function create_instructor_confirmation(attendance){
        let response=await axios.post('/adminmaker/create_instructor_confirmation/',{student_id:data.student.id,attendance_id:attendance.id})
        Object.assign(attendance,response.data)

        assign_bad_attendance()
    }

    async function delete_instructor_confirmation(confirmation,attendance){
        let response=await axios.post('/adminmaker/delete_instructor_confirmation/',{student_id:data.student.id,confirmation_id:confirmation.id, attendance_id:attendance.id})
        Object.assign(attendance,response.data)
        assign_bad_attendance()
    }


    async function create_student_confirmation(attendance){
        let response=await axios.post('/adminmaker/create_student_confirmation/',{student_id:data.student.id,attendance_id:attendance.id})
        Object.assign(attendance,response.data)
        assign_bad_attendance()
    }

    async function delete_student_confirmation(confirmation,attendance){
        let response=await axios.post('/adminmaker/delete_student_confirmation/',{student_id:data.student.id,confirmation_id:confirmation.id,attendance_id:attendance.id})
        Object.assign(attendance,response.data)
        assign_bad_attendance()
    }


    async function update_attendance_package(e,attendance,package_,payment){
        let package_id=e.target.value
        console.log(package_id)
        let response=await axios.post('/adminmaker/update_attendance_package/',{student_id:data.student.id,package_id:package_id,attendance_id:attendance.id})
        // Object.assign(data.payments,response.data)
        data.payments=response.data

        // if(payment){
        //     payment.show=true
        // }
        assign_bad_attendance()

    }


    async function make_monthly(payment){
        let response=await axios.post('/adminmaker/make_monthly/',{student_id:data.student.id,query_datetime:payment.datetime})
        // Object.assign(data.payments,response.data)
        data.payments=response.data

    }

    async function make_all_monthly(){
        let response=await axios.post('/adminmaker/make_all_monthly/',{student_id:data.student.id})
        // Object.assign(data.payments,response.data)
        data.payments=response.data

    }

    async function all_into_one(){
        let response=await axios.post('/adminmaker/all_into_one/',{student_id:data.student.id})
        Object.assign(data.payments,response.data)
        data.payments=response.data
    }

    async function default_datetimes(payment){
        let response=await axios.post('/adminmaker/default_datetimes/',{student_id:data.student.id,payment_id:payment.id})
        Object.assign(data.payments,response.data)
        data.payments=response.data
    }

    async function delete_duplicate_datetimes(payment){
        let response=await axios.post('/adminmaker/delete_duplicate_datetimes/',{student_id:data.student.id,payment_id:payment.id})
        Object.assign(data.payments,response.data)
        data.payments=response.data
    }
    

    async function fix_in_packages(){
        let response=await axios.post('/adminmaker/fix_in_packages/',{student_id:data.student.id})
        Object.assign(data.payments,response.data)
        data.payments=response.data
    }





    function student_dashboard(student){

        router.push({
            path: '/student-dashboard',
            query: {user_id:student.user}
        });
    }









    async function show_payment(payment){
        let response = await axios.post('/manager/get_payment/',{payment_id:payment.id})

        Object.assign(payment,response.data)
        console.log(payment.show    )
        payment.show=!payment.show
    }





















</script>




<style scoped>

    .container-payments{
        width: 0;
        height: 0;
        display: flex;
        flex-direction: column;
        align-items:center;
        gap:1rem;
        overflow:hidden;
        max-width: 100%;

    }

    .fullscreen{
        position: fixed;
        top:0;
        background: var(--gray);
        width: 100vw;
        max-width: 100vw;

        height: 100vh;
        overflow: auto;
        
    }

    .payment{
        background: var(--red2);
        color:var(--black);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap:1rem;
        border: 5px solid var(--blue2);
        min-width: fit-content;
        max-width: 80vw;
        padding: 1rem;
        min-height: 20%;
        max-height: 100%;
        overflow: auto;
    }


    .payment-title{
        max-width: 100%;
        text-align: center;
        text-justify: center;
        font-size: xx-large;
        padding: 1rem;
        background: var(--white);

    }





    .show_payment{
        min-height: 80%;
    }    

    

    .paid{
        background:var(--green1);
    }

    .edit-payment{
    }

    .edit-payment label{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 100%;
    }

    .packages{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap:1rem;
        max-width: 100%;
    }

    .package{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap:1rem;
        max-width: 100%;

    }

    .edit-package{
        border-radius: 1rem;
        max-width: 100%;

    }

    .attendances{
        display: flex;
        flex-direction: column;
        gap:1rem;
        align-items: center;
        align-content: center;
        max-width: 100%;

    }


    .attendance{
        background: var(--white1);
        align-items: center;
        backdrop-filter: opacity(0.4);

    }

    .bad-attendance{
        display: flex;
        flex-direction: row;
        background: var(--white1);
        align-items: center;
        backdrop-filter: opacity(0.4);
    }



    .instructor-confirmations{
        display: flex;
        flex-direction: column;
        align-items: center;

    }

    .instructor-confirmations-title{
        display: flex;
    }

    .instructor-confirmation{
        display: grid;
        grid-template-areas: 
                            "title buttons"
                            "confirmation buttons";
        align-items: center;
    }

    .instructor-confirmation-title{
        grid-area: title;
    }







    .student-confirmations-title{
        display: flex;
    }
    .student-confirmations{
        display: flex;
        flex-direction: column;
        align-items: center;

    }

    .student-confirmation{
        display: grid;
        grid-template-areas: 
                            "title buttons"
                            "confirmation buttons";
        align-items: center;
        margin-bottom: 0.5rem;
    }


    .student-confirmation-title{
        grid-area: title;
    }










    .confirmation{
        grid-area: confirmation;
    }




    button{
        height: 1.5rem;
        width: 1.5rem;
        border: 5px solid var(--black)
    }

    .add{
        background: var(--green1);
    }

    .delete{
        background: var(--red2);
        grid-area: buttons;
    }

    .make_monthly{
        width: fit-content;
        padding: 1rem;
        border-radius: 1rem;
        border: 5px solid var(--yellow1);
        color: var(--black);
    }

    @media (max-width:1000px) {
        table{
            align-self: start;
        }

        .packages{
            align-self: start;

        }
        .package{
            align-self: start;
        }

        .attendances{
            align-self: start;
        }

    }

    table {
        border-collapse: separate;
        border-spacing: 0;

    }

    tr{
        border-radius: 1rem;
        overflow: hidden;
    }

    td{
        text-align: center;
        text-justify: center;
        border-top: 10px solid var(--black);
        border-bottom: 10px solid var(--black);

    }

    select, input{
        border-radius: 1rem;
        font-size: large;
        padding: 0.5rem;
        text-align: center;
    }
    



</style>
<template>
  <TutorialScreen ref="tutorial_screen"/>

  <div class="groups">
    <!-- {{ instructor }} -->
    <div class="group" v-for="group in groups">
      <button @click.stop="infoshow(group)" class="group-title"> 
        <template v-for="student in group.student">
          {{ student.ui }}. 
        </template>
      </button>

      <div v-show="group.infoshow" class="group-info">
        <div>
          Instructor
        </div>
        <hr>
        <div>
          {{ instructor.ui }}

        </div>

        <br>
        <div>Student</div>
        <hr>
        <div v-for="student in group.student">{{ student.ui }}.</div>

        <br>
        <div>Material</div>
        <hr>
        <div v-for="material in group.attendance.iamaterial" v-if="group.attendance">
          {{material.ui }}
        </div>
        <br>
        <div>Schedule</div>
        <hr>
        <div>{{ group.schedule }}</div>

        <br>
        <div>Duration</div>
        <hr>
        <div>{{ group.duration }}</div>


      </div>


      <div class="attendance-buttons">
        <button @click.stop="class_status(group,'confirmed')">Confirm</button>
        <button @click.stop="class_status(group,'cancelled-late')">Cancel Late</button>
        <button @click.stop="class_status(group,'cancelled-on-time')">Cancel On Time</button>
        <button @click.stop="class_status(group,'reschedule')">Reschedule</button>
        <button @click.stop="class_status(group,'no-show')">No Show</button>


      </div>
      <div class="attendance">
        <template v-if="group.attendance">
          <template v-for="student in group.student">
            <template v-if="student.confirmation">
              <div class="confirmation" :class="student.confirmation.confirmation" >
                {{ student.confirmation.ui }}
              </div>
            </template>
            <template v-else>
              <div class="confirmation">
                {{ student.ui }}: has not confirmed

              </div>
            </template>
          </template>
        </template>

        <template v-if="group.instructor_confirmation"> 
          <div class="confirmation" :class="group.instructor_confirmation.confirmation" v-if="group.instructor_confirmation">
            {{ group.instructor_confirmation.ui }}
            <a v-if="group.instructor_confirmation.confirmation=='confirmed'">
              <button @click.stop="join_class(group.attendance.link,group.link)" class="join-button"> Join Class </button>
            </a>
            <template v-if="group.instructor_confirmation.confirmation=='confirmed' && group.link.includes('zoom') || group.link.includes('meet')">
              <div>
                {{ group.link }}
              </div>
            </template>
            <template v-else-if="group.instructor_confirmation.confirmation=='confirmed' && !group.link.includes('zoom') && !group.link.includes('meet')">
              <div>
                {{ group.attendance.link }}
              </div>
            </template>
          </div>
          </template>
          <template v-else>
            <div class="confirmation">
              You have not confirmed this class.
            </div>

          </template>


      </div>
    </div>




  </div>


  <Calendar/>
  
  <Confirm ref="confirm" />




</template>


<script setup>
  import TutorialScreen from '@/components/TutorialScreen.vue'


  import {ref,reactive, provide, onMounted,onBeforeMount} from 'vue'
  import Confirm from '@/components/Confirm.vue'
  import Calendar from '@/components/Calendar.vue'
  import {useRoute,useRouter} from 'vue-router'
  import {useStore} from 'vuex'
  import axios from 'axios'


  let store=useStore()

  let gaby="Gabriela Mondragon" // <- string
  let gaby= 1234
  let gaby = ['Fer','Diego','Nabil','mama']
  let gaby = {
    nombre_completo: "Gabriela Mondragon",
    id_estudiantil: 1234,
    gente_que_le_cae_bien:['Fer','Diego','Nabil','mama'];
  }


  let user=store.state.user
  let router = useRouter()
  let instructor=ref()
  let groups=ref()

  let confirm=ref()
  let attendance=reactive({})
  let confirm_group=reactive({})

  let tutorial_screen=ref()

  provide('attendance',attendance)
  provide('confirm_group',confirm_group)
  provide('user',user)

  let route=useRoute()


  onBeforeMount(()=>{

    if (user.role.includes('Admin')){

      console.log(route.query.user_id)
      let user_id=route.query.user_id
      
      
      user.id=user_id

    }



  })


  // onBeforeMount(()=>{

  //   if (user.role.includes('Admin')){
  //     let instructor_id=prompt('user id')
      
  //     user.id=instructor_id

  //   }
  // })

  onMounted(()=>{
    user=store.state.user

    
    get_instructor()
    
    recursive_attendance()
    

  }
  
  
  )


  function recursive_attendance(){
    setTimeout(() => {
      if(window.location.href.includes('instructor')){
        get_attendances()
        recursive_attendance()
      }
    }, 20000);

  }



  async function get_instructor(){

    let response=await axios.post('/instructors/get_instructor/',{userid:user.id})
    // let response=await axios.post('/instructors/get_instructor/',{userid:2})
    // let response=await axios.post('/students/get_student/',{userid:2})
    instructor.value=response.data

    groups.value=instructor.value.group_set


    get_attendances()
    check_tutorial()


  }

  async function get_attendances(){


    groups.value.forEach(async (group)=>{
      let response=await axios.post('/instructors/get_attendance/',{groupid:group.id})

      group.attendance=response.data
      if ('none' in group.attendance){
        group.attendance=null
        return
      }
      
      group.student.forEach(student=>{
        student.confirmation=group.attendance.student_confirmation.filter(confirmation=>confirmation.student.id==student.id)
        student.confirmation.sort((a,b)=>{
          return a.id-b.id
        })
        student.confirmation=student.confirmation.at(-1)


      })


      group.instructor_confirmation=group.attendance.instructor_confirmation.filter(confirmation=>confirmation.instructor.id==instructor.value.id)
      group.instructor_confirmation.sort((a,b)=>{
        return a.id-b.id
      })
      group.instructor_confirmation=group.instructor_confirmation.at(-1)


    })



  }

  async function class_status(group,status){
    
    let response= await axios.post('/instructors/class_status/',{userid:user.id,groupid:group.id,status:status})
    get_attendances()
    if(['confirmed','cancelled-late','no-show'].includes(status)){
      
      showattendanceconfirmation(group)
      
    }
        
  }
      
  async function showattendanceconfirmation(group){
    attendance.data=await get_attendance(group.id)
    confirm_group.data=group
    console.log('pasting',attendance.data,confirm_group)

    confirm.value.show=true

  }

  async function get_attendance(groupid){
    let response=await axios.post('/instructors/get_attendance/',{groupid:groupid})
    console.log(response.data)
    return response.data
  }



  function infoshow(group){
    group.infoshow=!group.infoshow
  }


  function join_class(attendance_link,group_link){

window.location.href=attendance_link

// router.push({ name: 'meet',params:{link:attendance_link}});



}


function check_tutorial() {

  console.log('CHECKING TUTORIAL')
  console.log(instructor.value.user.tutorial)
  if (instructor.value.user.tutorial == true) {
    return
  } else {
    setTimeout(() => {
      playtutorial()
    }, 1000);
  }

}


class TutorialElement {
  constructor(element, positiondescription, message) {
    console.log('CONSTRUCTING')
    this.element = element
    this.message = message
    this.positiondescription = positiondescription
  }

  focus(delay) {
    setTimeout(() => {

      let tutorial_elements = document.getElementsByClassName('tutorial-focus')
      Array.from(tutorial_elements).forEach(tutorial_element => {
        tutorial_element.classList.remove('tutorial-focus')
      })

      console.log(this.element)
      this.element.classList.add('tutorial-focus')
      tutorial_screen.value.message = this.message

      if (this.positiondescription == 'center') {
        this.midcoordinates()
        window.scrollTo({ top: this.position, behavior: "smooth" })
      } else {
        this.element.scrollIntoView({ behavior: "smooth" })

      }


    }, 5000 * delay)
  }

  midcoordinates() {
    this.top = this.element.getBoundingClientRect().top + window.pageYOffset


    let viewportHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);

    this.position = this.top - viewportHeight / 2

  }

}

let playtutorial = async () => {


  tutorial_screen.value.show = true

  let focus_elements = [

    new TutorialElement(document.getElementsByClassName(
      'group-title')[0],
      'center',
      'Click here to expand group information.'
    ),



    new TutorialElement(document.getElementsByClassName(
      'attendance-buttons')[0],
      'center',
      'Click here to confirm, cancel or change the confirmation of the class.'
    ),
    new TutorialElement(document.getElementsByClassName(
      'attendance')[0],
      'center',
      'Here you can view the confirmation status for your students and JOIN the class.'
    ),


  ]



  console.log(focus_elements)

  focus_elements.forEach((focus_element, index) => {

    focus_element.focus(index)

  })
  setTimeout(async () => {

    let tutorial_elements = document.getElementsByClassName('tutorial-focus')
    Array.from(tutorial_elements).forEach(tutorial_element => {
      tutorial_element.classList.remove('tutorial-focus')
      tutorial_screen.value.show = false
    })
    window.scrollTo({ top: 0, behavior: 'smooth' })

    await axios.post('/instructors/update_tutorial/', { instructorid: instructor.value.id })



  }, 5000 * focus_elements.length)
}





</script>











<style scoped>


  .tutorial-focus{

  z-index:52;


  animation-name: tutorial-focus;
  animation-duration: calc(var(--home)/4);
  animation-timing-function: ease-in-out;
  /* animation-delay: calc(var(--home)*5); */
  animation-iteration-count: infinite;
  animation-direction: alternate;
  animation-fill-mode:both;



  }


  @keyframes tutorial-focus {
  0%{
    border: 10px solid var(--green1);

  }
  100%{
    border: 10px solid var(--red3);
  }

  }












  .groups{
    max-width: 100%;
    min-height: 100vh;
    display: grid;
    align-items: center;
    justify-content: center;
    grid-template-columns: repeat(auto-fit,minmax(20rem,30rem));
    gap:1rem;
    background: var(--red1);
    
  }




  .group{
    background: var(--black);
    max-width: 100%;

    /* height: 20rem; */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    text-align: center;
    border: 5px var(--black) solid;
    border-radius: 2rem;
    overflow:hidden;

  }

  .group-title{
    font-size: x-large;
    width: 100%;

    border: 5px var(--black) solid;
    border-radius: 2rem;

  }

  .group-info{
    background: var(--black);
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    font-size: large;
    align-items: center;
    color:var(--white1);
    /* justify-content: center; */
    /* justify-items: center; */
    /* text-align: center; */
  }

  hr{
    /* align-self: center; */
    justify-self: center;
    height: 0px;
    width: 25%;
  }




  .attendance-buttons{
    background: var(--black);
    height: 5rem;
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;

  }
  .attendance-buttons button{
    height: 3rem;
    padding:3px;
    border-radius: 10px;
  }


  .attendance{
    width: 100%;
    height: 5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    

  }



  .join-button{
    width: fit-content;
    background: var(--blue1);
    color:var(--white1);
    padding: 5px;
    border-radius: 1rem;
    border:2px solid var(--white1);
    text-align: center;
    font-size: x-large;
    font-family:var(--passion);
  }

  .confirmation{
    display:flex;
    color: var(--white1);
    align-items: center;
    justify-content: space-around;
    width: 100%;
    height: 100%;
    background: var(--gray);
    text-align: center;
    
  }



  .confirmed{
    background:green;
  }

  .cancelled-on-time{
    background: blue;
  }

  .cancelled-late{
    background:red;
  }

  .no-show{
    background:red;
  }



</style>
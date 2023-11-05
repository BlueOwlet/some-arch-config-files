<template>
    <div class="message-manager">
        <div class="title">
            Initial Message Maker
        </div>
        <input @input.stop="search_users" class="user-search-input" v-model="users.searchpattern">
        <div class="search-results">
            <template v-if="users.users">
                <div class="result" @click.stop="create_message(user)" v-for="user in users.users">
                    {{ user.ui }}
                </div>
            
            </template>
        </div>
        <textarea class="message" v-model="users.current_message">

        </textarea>
    </div>

</template>



<script setup>

    import axios from 'axios'

    import {reactive} from 'vue'

    let users=reactive({
        searchpattern:'',
        users:null,
    })

    async function search_users(){

        let response=await axios.post('/dashboard/search_users/',{searchpattern:users.searchpattern})
        users.users=response.data
        console.log(users)
        Array.from(users.users).forEach(user=>{

            let password=`${user.first_name.slice(0,2).toLowerCase()}${user.last_name.slice(0,2).toLowerCase()}2023`

            user.message=`Hola ${user.first_name},

Nos comunicamos para informarte que para ingresar a tu primera clase deberás utilizar el siguiente usuario y contraseña una vez que el Teacher mande el link de confirmación en el grupo de Whatsapp:

usuario:
${user.username}
contraseña:
${password}

De igual manera podrás consultar el número de clases registradas el en sistema.
            
Para acceder a la plataforma debes dar click al link e ingresar con el siguiente usuario y contraseña:

https://interactspeakingcenter.com/login/



En caso de requerir ayuda para ingresar mandar mensaje de whatsapp en este chat.
            
            `
        })

    }

    function create_message(user){
        users.current_message=user.message
    }

</script>



<style scoped>

    .title{
        font-size: xxx-large;

    }

    .message-manager{
        display: grid;
        justify-content: center;
        justify-items: center;
        align-items: center;
        width: 100vw;
        gap:1rem;

    }
    .user-search-input{
        border-radius: 1rem;
        height: 3rem;
        font-size: x-large;
    }

    .search-results{
        display: grid;
        gap: 1rem;
        /* grid-template-columns: repeat(auto-fill,10rem); */

    }

    .result{
        border-radius: 1rem;
        border: 5px solid var(--green1);
        background:var(--blue1);
        color: var(--white1);
        font-size: xx-large;

    }

    .message{
        background: var(--black);
        color:var(--white1);
        border-radius: 1rem;
        width:min(100vw,20rem);
        height: 20rem;
        padding:1rem;
        font-size: large;
    }


</style>
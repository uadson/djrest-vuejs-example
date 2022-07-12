<template>
    <div>
        <p>Componente de Mensagem</p>
        <div>
            <form id="burger-form">
                <div class="input-container">
                    <label for="name">Cliente:</label>
                    <input type="text" id="name" name="name" v-model="name" placeholder="Digite seu nome">
                </div>
                <div class="input-container">
                    <label for="bread">Escolha o pão:</label>
                    <select name="breads" id="breads" v-model="breads">
                        <option value="">Selecione o tipo de pão</option>
                        <option v-for="bread in BreadsAPIData" :key="bread.id" :value="bread.name">
                            {{ bread.name }}
                        </option>
                    </select>                    
                </div>
                <div class="input-container">
                    <label for="meat">Escolha o carne do seu burger:</label>
                    <select name="meats" id="meats" v-model="meats">
                        <option value="">Selecione o tipo de carne</option>
                        <option v-for="meat in MeatsAPIData" :key="meat.id" :value="meat.name">
                            {{ meat.name }}
                        </option>
                    </select>                    
                </div>
               <div id="optional-container" class="input-container">
                    <label id="optional-title" for="optional">Selecione os opcionais:</label>
                    <div class="checkbox-container" v-for="option in OptionsAPIData" :key="option.id">
                        <input type="checkbox" name="options" v-model="options" :value="option.name">
                        <span>{{ option.name }}</span>
                    </div>                  
                </div>
                <div class="input-container">
                    <button class="submit-btn">Criar meu Burger</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
    name: 'BurgerForm',

    data() {
        return {
            BreadsAPIData: [],
            MeatsAPIData: [],
            OptionsAPIData: [],
        }
    },

    created() {
        getAPI.get('/breads/',)
            .then(response => {
                console.log('Breads API has recieved data')
                this.BreadsAPIData = response.data
            })
            .catch(err => {
                console.log(err)
            })

        getAPI.get('/meats/',)
            .then(response => {
                console.log('Meats API has recieved data')
                this.MeatsAPIData = response.data
            })
            .catch(err => {
                console.log(err)
            })

        getAPI.get('/options/',)
            .then(response => {
                console.log('Options API has recieved data')
                this.OptionsAPIData = response.data
            })
            .catch(err => {
                console.log(err)
            })
    }

    // data() {
    //     return {
    //         breads: null,
    //         /*
    //         meats: null,
    //         optionaldata: null,
    //         name: null,
    //         bread: null,
    //         meat: null,
    //         optional: null,
    //         status: null,
    //         msg: null
    //         */
    //     }
    // },

    // mounted() {
    //     this.getBreads();
    // },

    // methods: {
    //     // First Idea
    //     async getBreads() {
    //         axios ({
    //             method: 'GET',
    //             url: 'http://127.0.0.1:8000/api/app/v1/breads/',
    //         }).then(response => this.breads = response.data)
    //     }

    // }
}
</script>

<style scoped>
 #burger-form {
    max-width: 400px;
    margin: auto;
 }

 .input-container {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
 }

 label {
    font-weight: bold;
    margin-bottom: 15px;
    color: #222;
    padding: 5px 10px;
    border-left: 4px solid #FCBA03;
 }

 input, select {
    padding: 5px, 10px;
    width: 300px;
 }

 #optional-container {
    flex-direction: row;
    flex-wrap: wrap;
 }

 #optional-title {
    width: 100%;
 }

.checkbox-container {
    display: flex;
    align-items: flex-start;
    width: 50%;
    margin-bottom: 20px;
}

.checkbox-container span,
.checkbox-container input {
    width: auto;
}

.checkbox-container span {
    margin-left: 6px;
    font-weight: bold;
}

.submit-btn {
    background-color: #222;
    color:#FCBA03;
    font-weight: bold;
    border: 2px solid #222;
    padding: 10px;
    font-size: 16px;
    margin: 0 auto;
    cursor: pointer;
    transition: .5s;
}

.submit-btn:hover {
    background-color: transparent;
    color: #222;
}
</style>
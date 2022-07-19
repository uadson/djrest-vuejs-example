<template>
    <div>
        <p>Componente de Mensagem</p>
        <div>
            <form id="burger-form" @submit.prevent="addBurger">
                <div class="input-container">
                    <label for="name">Cliente:</label>
                    <input type="text" id="name" name="name" v-model="form.customer" placeholder="Digite seu nome" required>
                </div>
                <div class="input-container">
                    <label for="bread">Escolha o pão:</label>
                    <select name="breads" id="breads" v-model="form.bread">
                        <option value="">Selecione o tipo de pão</option>
                        <option v-for="bread in breadsAPIData" :key="bread.id" :value="bread.id">
                            {{ bread.name }}
                        </option>
                    </select>                    
                </div>
                <div class="input-container">
                    <label for="meat">Escolha o carne do seu burger:</label>
                    <select name="meats" id="meats" v-model="form.meat">
                        <option value="">Selecione o tipo de carne</option>
                        <option v-for="meat in meatsAPIData" :key="meat.id" :value="meat.id">
                            {{ meat.name }}
                        </option>
                    </select>                    
                </div>
               <div id="optional-container" class="input-container">
                    <label id="optional-title" for="optional">Selecione os opcionais:</label>
                    <div class="checkbox-container" v-for="option in optionsAPIData" :key="option.id">
                        <input type="checkbox" name="options" v-model="form.options" :value="option.id">
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
import api from '@/services/api.js'

export default {
    name: 'BurgerForm',

    data(){
        return{
            // Get API Data
            breadsAPIData: [],
            meatsAPIData: [],
            optionsAPIData: [],
           

            // Post Form API Data
            form: {
                customer: '',
                bread: '',
                meat: '',
                options: [],
            }
        }
    },

    mounted(){
        // Breads
        api.get('/breads/',)
            .then(response => {
                console.log('Breads api data received')
                this.breadsAPIData = response.data
            })
            .catch(err => {
                console.log(err)
            })

        // Meats
        api.get('/meats/',)
            .then(response => {
                console.log('Meats api data received')
                this.meatsAPIData = response.data
            })
            .catch(err => {
                console.log(err)
            })

        // Optional
        api.get('/options/',)
            .then(response => {
                console.log('Optional api data received')
                this.optionsAPIData = response.data
            })
            .catch(err => {
                console.log(err)
            })
    },
    methods:{
        addBurger(){
            api.post('/orders/', this.form)
            .then(response => {
                console.log(response.status)
                console.log('Burger created with success')
            })
            .catch(err => {
                console.log(err)
            })

            // send message


            // clean message


            // clean form
            this.form = ''
            
        }
    }

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
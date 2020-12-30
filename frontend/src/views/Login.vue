<template>
  <form @submit.prevent="login" class="mt-3" v-if="token ==null">
    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
    <input type="text" class="form-control" id="staticEmail" v-model="username">

    <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
    <input type="password" class="form-control" id="inputPassword" v-model="password">

    <input type="submit" value="Login" class="btn btn-primary ml-2">
  </form>
</template>

<script>
import axios from "axios";

export default {

  name: "Login",
  data(){
    return{
      username: '',
      password: '',
      token: null,
    }
  },

  methods: {

    login(){

      const data = {
        username: this.username,
        password: this.password,
      }
      axios.post('http://localhost:8000/auth/',data)
        .then(res => {
            this.token = res.data.token
            localStorage.setItem('user-token', this.token)
            this.$router.push({ name: 'to-do'})
        })
        .catch(() => {
          localStorage.removeItem('user-token')
        })
    }
  }
}
</script>

<style scoped>
  label{
    color:white;
  }
</style>

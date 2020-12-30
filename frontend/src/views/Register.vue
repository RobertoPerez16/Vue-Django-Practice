<template>
    <div>
      <h1 class="text-center mt-3">User Registration</h1>
      <div class="container mt-5">
        <form @submit.prevent="CreateUser">
          <div class="mb-3">
            <label for="user_text" class="form-label">UserName:</label>
            <input type="text" class="form-control" id="user_text" v-model="username">

          </div>
          <div class="mb-3">
            <label for="password_text" class="form-label">Password</label>
            <input type="password" class="form-control" id="password_text" v-model="password">
          </div>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>

</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data(){
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    CreateUser(){
      const data = {
        username: this.username,
        password: this.password,
      }

      axios.post("http://localhost:8000/api/users/", data)
      .then(()=> {
        this.$router.push({ name: 'home' })
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>

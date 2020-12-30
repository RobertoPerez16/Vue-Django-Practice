<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand">ToDoApp</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav" v-if="token==null">
            <router-link to="/register" class="nav-link">Register</router-link>
          </ul>
        </div>
        <login class="d-flex" v-if="token ==null"></login>

        <form class="d-flex" @submit.prevent="logOut" v-if="token!==null">
          <button type="submit" class="btn btn-danger">LogOut</button>
        </form>

      </div>
    </nav>
  </div>
</template>

<script>

import Login from "@/views/Login";
export default {
  name: "NavBar",
  components: {Login},
  data(){
    return {
      token: localStorage.getItem('user-token')
    }
  },
  methods: {
    logOut(){
      localStorage.removeItem('user-token')
      this.$router.push({ name: 'home' })
    }
  }
}
</script>

<style scoped>

</style>

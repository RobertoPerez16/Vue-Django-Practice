<template>
  <div class="container mt-3">
    <div class="card" v-if="token !==null ">
      <div class="card-body">
        <h6 class="mb-3">{{ title.title }}</h6>
        <form @submit.prevent="deleteTask">
          <button class="btn btn-danger">Delete</button>
        </form>

      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";
export default {
  name: "ShowList",
  props: ['title', 'id'],
  data(){
    return {
      token: localStorage.getItem('user-token')
    }
  },

  methods: {
    deleteTask(){
      axios.delete(`http://localhost:8000/api/to-do/${this.id}/`)
      .then((res) => {
        const id = res.data.id;
        this.$emit('delete', id)
      })
    }
  }

}
</script>

<style scoped>
  .container {
    width: 500px;
  }
</style>

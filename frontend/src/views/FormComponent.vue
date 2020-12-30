<template>
    <div class="container mt-3">
      <div class="card" v-if="user_token !== null">
        <div class="card-body">
          <form @submit.prevent="checkForm" >
            <label for="id_text">Write what you have to do</label>
            <input id="id_text" type="text" class="form-control" v-model="text_title" />
            <input type="submit" class="btn btn-success mt-3" value="Add" />
            <div class="text-center text-danger">{{ error }}</div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>

import axios from "axios";
export default {
  name: "FormComponent",
  data() {
    return {
      text_title: '',
      user_token: localStorage.getItem('user-token') || null,
      error: ''
    }
  },

  methods: {
    checkForm(){

      if(this.text_title.trim() === "") {
        this.error = "Error, you cannot send this field empty"
        setTimeout(()=> {
          this.error = ""
        }, 3000)


      }else{

        axios.post('http://localhost:8000/api/to-do/', {
          title: this.text_title,
        }).then(res => {
          const titles = res.data
          this.$emit('new', titles)
        })
        .catch(err => console.log(err))
        this.text_title = ""

      }

    }
  }
}
</script>

<style scoped>
  .container{
    width: 600px;
  }
</style>

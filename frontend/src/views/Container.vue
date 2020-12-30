<template>
  <div id="app">
    <NavBar />

    <FormComponent @new="addTitles"/>
    <ShowList
        v-for="title in titles"
        :key="title.id"
        :title="title"
        :id="title.id"
        @delete="removeTitles"
    />

  </div>
</template>

<script>

import FormComponent from "@/views/FormComponent";
import ShowList from "@/views/ShowList";
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
  name: 'Container',

  components: {
    NavBar,
    ShowList,
    FormComponent
  },

  data(){
    return{
      titles: []
    }
  },

  mounted() {
    axios.get("http://localhost:8000/api/to-do/")
        .then(res => {
          this.titles = res.data
        })
        .catch(err => console.log(err))
  },

  methods: {
    addTitles(title){
      this.titles = [...this.titles, title]
    },
    removeTitles(id){
      this.titles.splice(id,1)
    }
  }
}
</script>

<style>

</style>

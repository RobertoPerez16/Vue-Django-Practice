import Vue from "vue"
import VueRouter from "vue-router";

import Container from "@/views/Container";
import NavBar from "@/components/NavBar";
import Register from "@/views/Register";

//Components//

Vue.use(VueRouter)

const routes = [

    {
        path: '/',
        component: NavBar,
        name: "home",
    },
    {
        path: '/to-do',
        component: Container,
        name: "to-do",
    },
    {
        path: '/register',
        component: Register,
        name: "register"
    }

]

const router = new VueRouter({
    mode: "history",
    routes
})

export default router

import {createRouter, createWebHistory} from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Hotel from './views/Hotel.vue'
import Contact from './views/Contact.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'

const routes = [
    {path: '/', component: Home},
    {path: '/about', component: About},
    {path: '/contact', component: Contact},
    {path: '/hotels', component: Hotel},
    {path: '/login', component: Login},
    {path: '/register', component: Register},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
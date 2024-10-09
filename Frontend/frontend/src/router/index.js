import { createRouter, createWebHistory } from 'vue-router';
//import Home from '../views/Home.vue';
//import About from '../views/About.vue';
import Get_all_objects from '@/components/get_all_objects.vue';
import Product_page from '@/views/product_page.vue';
import Shopping_cart from '@/views/shopping-cart_page.vue';
import Login_page from '@/views/login_page.vue';
import Register_page from '@/views/register_page.vue';

const routes = [
  {
    path: '/',
    name: 'product_page',
    component: Product_page
  },

  {
    path: '/api_test',
    name: 'API',
    component: Get_all_objects
  },

  {
    path: '/shopping-cart',
    name: 'shopping-cart',
    component: Shopping_cart
  },

  {
    path: '/login-page',
    name: 'login-page',
    component: Login_page
  },

  {
    path: '/register-page',
    name: 'register-page',
    component: Register_page
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;

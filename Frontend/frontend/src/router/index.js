import { createRouter, createWebHistory } from 'vue-router';
//import Home from '../views/Home.vue';
//import About from '../views/About.vue';
import Get_all_objects from '@/components/get_all_objects.vue';
import Product_page from '@/views/product_page.vue';

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
  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;

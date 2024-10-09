import { createRouter, createWebHistory } from 'vue-router';
import Get_all_objects from '@/components/get_all_objects.vue';
import Get_all_orders from '@/components/get_orders_by_customerid.vue';
import Product_page from '@/views/product_page.vue';
import Shopping_cart from '@/views/shopping-cart_page.vue';
import Login_page from '@/views/login_page.vue';
import Register_page from '@/views/register_page.vue';
import ApiPage from '@/components/Apipage.vue';
import Get_Object from '@/components/get_object.vue';

const routes = [
  {
    path: '/', // Hauptseite (Startseite)
    name: 'product_page',
    component: Product_page
  },
  {
    path: '/api_test',   // Hauptpfad für die API-Seite
    component: ApiPage,  // Hauptkomponente für verschachtelte Routen
    children: [
      {
        path: 'objects',  // Verschachtelte Route für /api_test/objects
        name: 'GetAllObjects',
        component: Get_all_objects
      },
      {
        path: 'orders',  // Verschachtelte Route für /api_test/orders
        name: 'GetAllOrders',
        component: Get_all_orders
      },
      {
        path: 'object',
        name: 'GetObject',
        component: Get_Object
      }
    ]
  },
  {
    path: '/shopping-cart',  // Einkaufswagen-Seite
    name: 'shopping-cart',
    component: Shopping_cart
  },
  {
    path: '/login-page',  // Login-Seite
    name: 'login-page',
    component: Login_page
  },
  {
    path: '/register-page',  // Registrierungs-Seite
    name: 'register-page',
    component: Register_page
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
<template>
    <div>
      <h1>API Test Page</h1>
     
      <router-link to="/api_test/objects">Get All Objects</router-link> | 
      <router-link to="/api_test/orders">Get All Orders</router-link>
      <router-link to="/api_test/object">Get an Object</router-link>

      <router-view></router-view>
    </div>
  </template>
  
  <script>

  export default {
    name: 'ApiPage'
  };
  </script>
  
  <style scoped>
  /* Styles für die API-Seite */
  </style>
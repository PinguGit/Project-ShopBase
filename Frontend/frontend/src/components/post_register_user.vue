<template>
    <div>
   
    </div>
  </template>
  
  <script>
  export default {

    props: ['form'],

    name: "post_user",
    
    methods: {

      async post_register_user() {
        try {
          const response = await fetch(`${this.host}api/registerUser`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.form),
          });
  
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
  
          const data = await response.json();
          console.log("Successfully registered", data);
  
        } catch (error) {
          console.error('Error during registration:', error);
        }
      }
    }
  };
  </script>
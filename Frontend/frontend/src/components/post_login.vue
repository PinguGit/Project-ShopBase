<template>
    <div>
   
    </div>
  </template>
  
  <script>
  export default {

    props: ['form_login'],

    name: "post_user",
    
    host: 'http://127.0.0.1:5000/',
    
    methods: {

      async post_login_user() {
        try {
          const response = await fetch(`http://127.0.0.1:5000/api/loginUser`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.form_login),
          });
  
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
  
          const data = await response.json();


          // Return Result of API back to parent who called

          this.$emit('response', data)
          
          console.log("Successfully signed in", data);
  
        } catch (error) {
          console.error('Error during login:', error);
        }
      }
    }
  };
  </script>
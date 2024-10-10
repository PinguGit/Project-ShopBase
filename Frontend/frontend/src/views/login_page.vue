<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Product Page</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <div class="login-container">
            <h2>Login</h2>
            <form @submit.prevent="loginUser">
                <div id="email">
                    <i class="fas fa-user"></i>
                    <input type="text" v-model="email" placeholder="E-Mail" required>
                </div>
                <div class="password-class" id="password">
                    <i class="fas fa-lock"></i>
                    <input type="password" v-model="password" placeholder="Password" required>
                </div>
                <button type="submit" class="login-btn">
                    <i class="fas fa-sign-in-alt"></i> Login
                </button>
                <router-link to="/register-page">
                    <button type="button" class="register-btn">
                        <i class="fas fa-user"></i> Register
                    </button>
                </router-link>                
                
                <router-link style="text-decoration: none;" to="/">
                    <p class="back">zurück</p>
                </router-link>

                <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
            </form>
        </div>
    </body>
    </html>
</template>
  
<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: '' // Fehlermeldung hinzufügen
    };
  },
  methods: {
    async loginUser() {
      console.log("Login Button clicked"); // Log zum Testen
      const loginData = {
        email: this.email,
        entered_password: this.password,
      };

      try {
        console.log("Sending request to server..."); // Log vor dem fetch-Aufruf
        const response = await fetch('http://localhost:5000/api/loginUser', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(loginData)
        });

        const data = await response.json();
        console.log("Response received:", data); // Log der Serverantwort

        if (data.success) {
          console.log('Login successful');
          this.$router.push('/user-page');
        } else {
          console.log('Invalid credentials');
          this.errorMessage = 'Invalid credentials. Please try again.';
        }
      } catch (error) {
        console.error('Error during login:', error);
        this.errorMessage = 'An error occurred. Please try again later.';
      }
    }
  }
};
</script>

<style scoped>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
    }

    .login-container {
        display: inline-block;
        background-color: #fff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 300px;
        text-align: center;
    }

    h2 {
        margin-bottom: 10px;
    }

    .password-class {
        margin-bottom: 10px;
    }

    input[type="text"], input[type="password"] {
        width: 80%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .login-btn, .register-btn {
        width: 100%;
        padding: 10px;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .login-btn:hover {
        background-color: #0056b3;
    }

    .login-btn {
        background-color: #007bff;
        margin: 5px 0;
    }

    .register-btn {
        background-color: #28a745;
    }

    .register-btn:hover {
        background-color: #218838;
    }

    .login-container i {
        margin-right: 8px;
    }

    .error {
        color: red;
        margin-top: 10px;
    }

    .back {
        font-size: 10px;
        color: gray;
        text-align: left;
    }
</style>
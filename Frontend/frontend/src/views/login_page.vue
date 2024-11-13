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
            <form @submit.prevent="login">
                <div id="email">
                    <i class="fas fa-user"></i>
                    <input type="text" v-model="form_login.email" placeholder="E-Mail" required>
                </div>
                <div class="password-class" id="password">
                    <i class="fas fa-lock"></i>
                    <input type="password" v-model="form_login.entered_password" placeholder="Password" required>
                </div>
                    <div class="custom-radio">
                        <div class="radio-item">
                        <input type="radio" id="private" value="private" v-model="form_login.customerType" style="margin-bottom: 5px;">
                        <label for="private">Privatkunde</label>
                        </div>
                        
                        <div class="radio-item">
                        <input type="radio" id="business" value="business" v-model="form_login.customerType" style="margin-bottom: 5px;">
                        <label for="business">Händler</label>
                        </div>
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
                <post_login ref="post_login" :form_login="form_login" @response="handleResponse"/>
                <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
            </form>
        </div>
    </body>
    </html>
</template>
  
<script>
import post_login from '@/components/post_login.vue';

export default {
    name: "LoginPage",
    components: {
        post_login
    },
  data() {
    return {
        form_login: {
      email: '',
      entered_password: '',
      customerType: '',

      }
    };
  },
  methods: {
    login() {
        this.$refs.post_login.post_login_user();
    },
    handleResponse(response) {
        if (response.success === true) {
            alert("Login successfull")
            // link to login page
            this.$router.push('/login-page');
        }
        else if (response.success.error === "Email already exists") {
            alert("User already exists")
        }
        else if(response.success.error === true){
            alert("Failure by regestration")
        }
    }
    }
  }
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

.custom-radio {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin: 10px 0;
}

.radio-item {
    display: flex;
    align-items: center;
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
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
            <form>
                <div>
                    <i class="fas fa-user"></i>
                    <input type="text" placeholder="E-Mail" required>
                </div>
                <div>
                    <i class="fas fa-lock"></i>
                    <input type="password" placeholder="Password" required>
                </div>
                <button type="submit" class="login-btn"><i class="fas fa-sign-in-alt"></i> Login</button>
                <router-link to="/register-page">
                    <button type="button" class="register-btn">
                        <i class="fas fa-user"></i> Register
                    </button>
                </router-link>
            </form>
        </div>
    </body>
    </html>
</template>
  
<script>

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
        margin-bottom: 20px;
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
</style>
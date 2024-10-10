<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shopping Cart</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <div class="container">
            <router-link to="/">
                <div class="logo">
                    <img src="../assets/LogoReal.png" alt="Logo" height="100px" width="125px">
                </div>
            </router-link>
            <div class="search-bar">
                <input type="text" placeholder="Suche nach Produkten...">
            </div>

            <router-link style="text-decoration: none; color: black;" to="/login-page">
                <div class="profile">
                    <i class="fa-solid fa-user"> Profil</i>
                </div>
            </router-link>

            <router-link style="text-decoration: none; color: black;" to="/shopping-cart">
                <div class="basket">
                    <i class="fas fa-shopping-cart"> Warenkorb</i>
                </div>
            </router-link>

            <div class="article-container">
                <p>Einkaufswagen</p>
                <div class="articles">
                    <!-- Artikel hier hinzufügen (löschfunktion hinzufügen [menge maybe einstellen können?])  -->
                </div>
            </div>

            <div class="payment">
                <p>Zwischensumme <!--hier dann den {{ ... }}--></p>
                <button class="payment-continue">Zur Kasse gehen</button>
            </div>
        </div>
    </body>
    </html>
</template>
  
<script>

</script>

<style scoped>
/* Importieren Sie Ihr CSS oder fügen Sie es direkt ein */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f8f9fa; /* Light background for contrast */
    color: #343a40; /* Dark text for readability */
}

.container {
    display: grid;
    grid-template-columns: 200px 1fr 150px 150px;
    grid-template-rows: 100px 1fr;
    grid-template-areas:
        "logo search-bar basket profile"
        "filter product-list product-list product-list";
    gap: 15px;
    height: 100vh;
    padding: 10px 20px 20px 20px;
}

.logo {
    grid-area: logo;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #495057; /* Dark background */
    border-radius: 50%;
    padding: 10px;
    width: 200px;
    height: 100px;
}

.search-bar {
    grid-area: search-bar;
    display: flex;
    justify-content: center;
    align-items: center;
}

.search-bar input {
    width: 90%;
    padding: 10px;
    font-size: 16px;
    border-radius: 25px; /* More rounded corners */
    border: 1px solid #6c757d;
    background-color: #fff;
    color: #495057;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.search-bar input:focus {
    border-color: #007bff; /* Highlight border on focus */
    outline: none;
    box-shadow: 0 4px 8px rgba(0, 123, 255, 0.2);
}

.basket, .profile {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    border-radius: 10px;
    border: 1px solid #6c757d;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
    cursor: pointer;
    padding: 10px;
    height: 60px;
    margin-top: 15px;
}

.basket:hover, .profile:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.basket i, .profile i {
    color: #007bff;
    font-size: 12px;
}

.basket, .profile {
    font-size: 14px;
    color: #343a40;
}

.filter {
    grid-area: filter;
    background-color: #fff;
    border-radius: 10px;
    border: 1px solid #6c757d;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 15px;
}

.filter h4 {
    margin-bottom: 15px;
    color: #007bff;
}

.filter input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid #ced4da;
    background-color: #f8f9fa;
}

.product-list {
    grid-area: product-list;
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-table {
    width: 100%;
    border-collapse: collapse;
}

.product-table th, .product-table td {
    padding: 15px;
    text-align: center;
    border-bottom: 1px solid #dee2e6;
}

.product-table th {
    background-color: #343a40;
    color: #fff;
    font-weight: bold;
}

.product-table td {
    color: #495057;
}

.product-table tr:nth-child(even) {
    background-color: #f8f9fa;
}

.product-table tr:nth-child(odd) {
    background-color: #ffffff;
}

.product-table button {
    padding: 8px 12px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.product-table button:hover {
    background-color: #0056b3;
}

/* Additional hover and focus effects */
.search-bar input:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}



</style>
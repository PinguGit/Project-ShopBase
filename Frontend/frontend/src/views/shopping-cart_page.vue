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
            <div class="logo">
                <img src="../assets/LogoReal.png" alt="Logo" height="100px" width="125px">
            </div>
            <div class="search-bar">
                <input type="text" placeholder="Search Bar">
            </div>
            <div class="profile">
                <i class="fa-solid fa-user"> Benutzer</i>
            </div>
            <div class="basket">
                <i class="fas fa-shopping-cart"> Shopping Cart</i>
            </div>

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
    font-family: Arial, sans-serif;
}

.container {
    display: grid;
    grid-template-columns: 200px 1fr 150px 150px;
    grid-template-rows: 100px 1fr;
    grid-template-areas:
        "logo search-bar basket profile"
        "filter product-list product-list product-list";
    gap: 10px;
    height: 100vh;
}

.logo {
    grid-area: logo;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid black;
    background: #2c313d;
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
}

.basket {
    grid-area: basket;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid black;
}

.profile {
    grid-area: profile;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid black;
}

.basket, .profile {
    font-size: 12px;
    margin: 10px;
}

.filter {
    grid-area: filter;
    background-color: #f0f0f0;
    border: 1px solid black;
    padding: 10px;
    margin-top: 10px;
}

.product-list {
    grid-area: product-list;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

/* Product Boxes */
.product-box {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-auto-flow: column;
    align-items: center;
    border: 1px solid black;
    padding: 10px;
    background-color: #f0f0f0;
    width: 100%;
    justify-content: space-between;
}

.image-section {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 150px;
    margin-right: 20px;
}

.image {
    width: 100px;
    height: 100px;
    background-color: #ccc;
    text-align: center;
    line-height: 100px;
}

.info-section {
    display: grid;
    grid-column-start: 2;
    grid-column-end: 7;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(3, 1fr);
    height: 100%;
}

h3 {
    font-size: 18px;
    grid-column: 1 / -1;
}

.price-section {
    display: flex;
    align-items: center;
    grid-row: 2 / 4;
}

.price {
    font-size: 24px;
    font-weight: bold;
}

.seller, .delivery-date {
    font-size: 14px;
}

.seller {
    grid-column: 2 / 4; 
}

.delivery-date {
    grid-column: 2 / 4;
}

.stock {
    grid-column: 4 / 5;
    grid-row: 2 / 4;
}

.actions {
    display: flex;
    gap: 50px;
    grid-row: 2 / 4;
    grid-column: 5 / 7;
    justify-content: center;
}

button {
    padding: 10px;
    width: 200px;
    border: none;
    cursor: pointer;
}

.add-to-basket {
    background-color: #4CAF50;
    color: white;
}

.buy-now {
    background-color: #f44336;
    color: white;
}

</style>
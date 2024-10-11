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

            <div class="cart-container">
                <!-- Artikelbereich -->
                <div class="cart-content">
                    <div class="cart-item">
                        <div class="item-image">
                            <img src="../assets/LogoReal.png" alt="Artikelbild" width="100px" height="100px">
                        </div>
                        <div class="item-details">
                            <p class="item-title">Performance Pants Herren Schwarz (Größe 27W/32L)</p>
                            <p class="item-subtitle">Bestseller Nr. 1 - Bequeme Schwarze Hose Herren</p>
                            <p class="item-availability">Auf Lager</p>
                            <p class="item-size">Größe: 27W / 32L</p>
                            <p class="item-color">Farbe: Schwarz</p>
                            <div class="item-actions">
                                <label for="quantity">Menge: </label>
                                <input id="quantity" type="number" value="1" min="1">
                                <button>Löschen</button>
                            </div>
                        </div>
                        <div class="item-price">
                            <p>55,00 €</p>
                        </div>
                    </div>

                    <!-- hier weitere elemente dann so dies das ananas-->
                </div>

                <!-- Zahlungsbereich -->
                <div class="payment-section">
                    <p>Zwischensumme (1 Artikel): <strong>55,00 €</strong></p>
                    <button class="checkout-button">Zur Kasse gehen</button>
                </div>
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
        "cart-container cart-container cart-container cart-container";
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

/* Additional hover and focus effects */
.search-bar input:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.cart-container {
    grid-area: cart-container; /* Richtig gestellt von cart-contain zu cart-container */
    margin: 0 auto; /* Zentriert den Container */
    background-color: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
    display: flex; /* Flexbox hinzufügen */
    gap: 20px; /* Abstand zwischen Artikelbereich und Zahlungsbereich */
    width: 100%;
}

.cart-header {
    margin-bottom: 20px; /* Abstand zum nächsten Element */
}

.cart-header h2 {
    font-size: 24px;
    border-bottom: 1px solid #dee2e6;
    padding-bottom: 10px;
}

.cart-content {
    display: grid;
    grid-template-columns: 1fr 1fr; /* Artikel und Preisbereich */
    gap: 20px;
    width: 100%;
}

.cart-item {
    display: flex; /* Flex-Layout für Artikel */
    gap: 15px; /* Abstand zwischen Bild und Details */
    border-bottom: 1px solid #dee2e6; /* Trennlinie zwischen den Artikeln */
    border-top: 1px solid #dee2e6;
    padding: 10px 0; /* Vertikaler Abstand */
    height: 200px;
    grid-column: 1 / -1;
}

.item-image {
    display: flex;
    justify-content: center; /* Horizontales Zentrieren */
    align-items: center; /* Vertikales Zentrieren */
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    margin-left: 20px;
    width: 200px;
}

.item-image img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover; /* Bildverhältnis beibehalten */
}


.item-details {
    flex-grow: 1; /* Füllt den verfügbaren Platz */
}

.item-title {
    font-size: 18px;
    font-weight: bold;
}

.item-subtitle {
    font-size: 14px;
    color: #6c757d;
}

.item-availability {
    color: #28a745;
    margin: 10px 0;
}

.item-size,
.item-color {
    font-size: 14px;
}

.item-actions {
    margin-top: 10px;
}

.item-actions input {
    width: 50px;
    padding: 5px;
    margin-right: 10px;
    border-radius: 5px;
    border: 1px solid #dee2e6;
}

.item-actions button {
    background-color: transparent;
    color: #007bff;
    border: none;
    cursor: pointer;
}

.item-price {
    display: flex;
    align-items: flex-start;
    font-size: 18px;
    font-weight: bold;
}

.payment-section {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
    border: 1px solid #e0e0e0;
    width: 300px; /* Feste Breite für den Zahlungsbereich */
}

.payment-section p {
    font-size: 18px;
    margin-bottom: 20px;
}

.checkout-button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #ffffff;
    border: none;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.checkout-button:hover {
    background-color: #0053ac;
}


</style>
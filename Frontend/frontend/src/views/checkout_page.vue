<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bestellung aufgeben</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <div class="container">
            <router-link to="/">
                <div class="logo">
                    <img src="../assets/LogoReal.png" alt="Logo" height="100px" width="125px">
                </div>
            </router-link>
            <div class="text-checkout">
                <p>Bezahlen Sie hier!</p>
            </div>

            <router-link style="text-decoration: none; color: black;" to="/shopping-cart">
                <div class="basket">
                    <i class="fas fa-shopping-cart"> Warenkorb</i>
                </div>
            </router-link>

            <div class="cart-container">
                <!-- Artikelbereich -->
                <div class="cart-content">
                    <div class="payment-options">
                        <h3>Bezahlen mit</h3>
                        <div class="payment-option">
                            <input type="radio" id="credit-card" name="payment-method" value="credit-card" checked>
                            <label for="credit-card">Keditkarte</label>
                        </div>
                        <div class="payment-option">
                            <input type="radio" id="paypal" name="payment-method" value="paypal">
                            <label for="paypal">PayPal</label>
                        </div>
                        <div class="payment-option">
                            <input type="radio" id="cash-on-delivery" name="payment-method" value="cash-on-delivery">
                            <label for="cash-on-delivery">Nachnahme</label>
                        </div>
                    </div>
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
                    <button class="buy-button">Jetzt kaufen</button>
                    <p>Zwischensumme (1 Artikel): <strong>55,00 €</strong></p>
                    <p>Gesamtbetrag: <strong>Geld</strong></p>
                </div>
            </div>
        </div>
    </body>
    </html>
</template>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
}
.container {
    display: grid;
    grid-template-columns: 200px 1fr 150px 150px;
    grid-template-rows: 100px 1fr;
    grid-template-areas:
        "logo text-checkout text-checkout basket"
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

.text-checkout {
    grid-area: text-checkout;
    display: flex;
    text-align: center;
    font-size: 3rem;
    font-weight: bolder;
    justify-content: center;
    align-items: center;
}

.basket {
    grid-area: basket;
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
.basket:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.basket i {
    color: #007bff;
    font-size: 12px;
}

.basket {
    font-size: 14px;
    color: #343a40;
}

.cart-container {
    grid-area: cart-container;
    display: flex;
    max-width: 100%;
    background-color: white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
/* Left Side (Items and Payment Options) */
.cart-content {
    width: 70%;
    padding: 20px;
    border-right: 1px solid #e0e0e0;
}
.payment-options {
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
}
.payment-options h3 {
    margin-top: 0;
}
.payment-option {
    margin-bottom: 10px;
}
/* Cart Items */
.cart-item {
    display: flex;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e0e0e0;
}
.item-image img {
    width: 100px;
    height: 100px;
    margin-right: 20px;
}
.item-details {
    flex: 1;
}
.item-title {
    font-weight: bold;
}
.item-subtitle, .item-availability, .item-size, .item-color {
    color: #555;
    font-size: 0.9em;
    margin: 5px 0;
}
.item-actions {
    margin-top: 10px;
}
.item-actions input {
    width: 50px;
    text-align: center;
}
.item-price {
    font-weight: bold;
    font-size: 1.1em;
    align-self: center;
    margin-left: 20px;
}

.item-actions button {
    background-color: transparent;
    color: #007bff;
    border: none;
    cursor: pointer;
    margin-top: 0;
}

.payment-section {
    width: 30%;
    padding: 20px;
}

.buy-button {
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

.buy-button:hover {
    background-color: #0053ac;
}
</style>
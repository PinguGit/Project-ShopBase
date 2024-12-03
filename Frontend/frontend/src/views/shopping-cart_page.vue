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

            <div class="profile" @click="handleProfileClick">
                <i class="fa-solid fa-user"> Profil</i>
            </div>

            <router-link style="text-decoration: none; color: black;" to="/shopping-cart">
                <div class="basket">
                    <i class="fas fa-shopping-cart"> Warenkorb</i>
                </div>
            </router-link>

            <div class="cart-container">
                <!-- Artikelbereich -->
                <div class="cart-content" :style="gridStyle">
                    <div v-for="(item, index) in groupedCartItems" :key="index">
                        <div class="cart-item">
                            <div class="item-image">
                                <img :src="item.url_link" alt="Artikelbild">
                            </div>
                            <div class="item-details">
                                <p class="item-title">{{ item.produkt_name}}</p>
                                <div class="item-actions">
                                    <label for="quantity">Menge: </label>
                                    <input 
                                        id="quantity" 
                                        type="number" 
                                        v-model.number="item.anzahl"
                                        min="1"
                                        @change="updateQuantity(item)"
                                    >
                                    <button @click="removeFromCart(item)" style="width: 50px;">Löschen</button>
                                </div>
                            </div>
                            <div class="item-price">
                                <p>{{ (item.preis * item.anzahl).toFixed(2) }} €</p>
                            </div>
                        </div>
                    </div>
                
                    <!-- Zahlungsbereich -->
                    <div class="payment-section">
                        <p>Zwischensumme {{  totalItems }} Artikel: <br>
                            <strong>{{  totalAmount.toFixed(2) }} €</strong></p>
                        <router-link to="/checkout-page">
                        <button class="checkout-button">Zur Kasse gehen</button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
</template>
  
<script>
import { useCartStore } from '@/stores/cart';
import { computed } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'ShoppingCart',
    setup() {
        const cartStore = useCartStore();

        const router = useRouter();

        // Greife auf die aktiven Produkte im Warenkorb zu
        const cartItems = computed(() => cartStore.activ_products_shoppingcart);


        // Gruppiere die Produkte und zähke die Menge pro Produkt
        const groupedCartItems = computed(() => {
            const uniqueItems = [];
            cartItems.value.forEach((item) => {
                const existingItem = uniqueItems.find(
                    (uniqueItem) => uniqueItem.produkt_name === item.produkt_name
                );
                if (existingItem) {
                    existingItem.quantity += item.anzahl || 1;
                } else {
                    uniqueItems.push({ ...item, quantity: item.anzahl || 1});
                }
            });
            return uniqueItems;
        });

        // Berechne die Gesamtanzahl der Artikel im Warenkorb
        const totalItems = computed(() => {
            return groupedCartItems.value.reduce((total, item) => total + item.anzahl, 0);
        });

        // Berechne den Gesamtpreis aller Artikel im Warenkorb
        const totalAmount = computed(() => {
            return groupedCartItems.value.reduce((total, item) => total + item.preis * item.anzahl, 0);
        });

        // Entferne einen Artikel aus dem Warenkorb,
        function removeFromCart(item) {
            const index = cartItems.value.findIndex(cartItem => cartItem.produkt_name === item.produkt_name);
            if (index > -1){
                cartStore.removeFromCart(index); // Entferne Produkt aus dem Store   
            }
        }

        // Aktualisiere die Menge im Warenkorb, wenn Benutzer die ändert
        function updateQuantity(item) {
            const NewQuantity = Math.max(item.anzahl, 1);
            const index = cartItems.value.findIndex(cartItem => cartItem.produkt_name === item.produkt_name);
            if (index > -1){
                cartStore.updateItemQuantity(index, NewQuantity);
            }
        }


        // grid-template-row Berechnung anhand der Anzahl im groupedCartItems
        const gridStyle = computed(() => {
            const rows = groupedCartItems.value.length > 0 ? `repeat(${groupedCartItems.value.length}, 200px)` : '200px';
            return {
                'grid-template-rows': rows
            };
        });

        // Funktion, die beim Klick auf das Profil ausgeführt wird
        function handleProfileClick() {
            const ablaufDatum = getCookieExpiryDate();
            if (ablaufDatum) {
                const currentDate = new Date();
                const expiryDate = new Date(ablaufDatum);

                // Vergleiche das Ablaufdatum mit der aktuellen Zeit
                if (expiryDate > currentDate){
                    router.push('/user-page');
                } else {
                    router.push('/login-page');
                }
            } else {
                console.error("Kein Ablaufdatum im Cookie gefunden");
                router.push('/login-page');
            }
        }

        function getCookieExpiryDate() {
            const cookies = document.cookie.split("; ");

            // Suche nach dem Cookie mit dem Ablaufdatum
            const expiryCookie = cookies.find(row => row.startsWith("customer_type_expiry="));

            // Wenn das Ablaufdatum-Cookie existiert, gibt es das Datum zurück
            if (expiryCookie) {
                return expiryCookie.split("=")[1];
            }
            return null;
        }

        return {
            groupedCartItems,
            totalItems,
            totalAmount,
            removeFromCart,
            gridStyle,
            updateQuantity,
            handleProfileClick
        };
    }
};
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
    display: flex;
    width: 100%;
    margin: 0 auto; /* Zentriert den Container */
    background-color: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 20px;
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
    grid-template-columns: 1fr 300px;
    grid-template-areas: 
        "items payment";
    grid-column-gap: 40px;
    width: 100%;
}

.cart-item {
    grid-area: items;
    display: flex; 
    gap: 15px; 
    border-bottom: 1px solid #dee2e6;
    border-top: 1px solid #dee2e6;
    padding: 10px 0; /* Vertikaler Abstand */
    height: 200px;
}

.item-image {
    display: flex;
    justify-content: center;
    align-items: center; 
    margin-left: 20px;
    width: 200px;
    height: 178px;
}

.item-image img {
    width: 100%;
    height: 100%;
    object-fit: contain; 
    margin: 0; 
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
    width: 100px;
}

.item-price p {
    text-align: right;
    width: 100%;
}

.payment-section {
    grid-area: payment;
    grid-row: 1/3;
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
    border: 1px solid #e0e0e0;
    width: 300px;
    align-self: flex-start;
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
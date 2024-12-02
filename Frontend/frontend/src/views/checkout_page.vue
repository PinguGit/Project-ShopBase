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
                            <input type="radio" id="credit-card" name="payment-method" value="credit-card" v-model="selectedPaymentMethod" checked>
                            <label for="credit-card">Keditkarte</label>
                        </div>
                        <div class="payment-option">
                            <input type="radio" id="paypal" name="payment-method" value="paypal" v-model="selectedPaymentMethod">
                            <label for="paypal">PayPal</label>
                        </div>
                        <div class="payment-option">
                            <input type="radio" id="cash-on-delivery" name="payment-method" value="cash-on-delivery" v-model="selectedPaymentMethod">
                            <label for="cash-on-delivery">Nachnahme</label>
                        </div>
                    </div>
                    <div v-for="(item, index) in groupedCartItems" :key="index">
                        <div class="cart-item">
                            <div class="item-image">
                                <img :src="item.url_link" alt="Artikelbild">
                            </div>
                            <div class="item-details">
                                <p class="item-title">{{ item.produkt_name}}</p>
                                <div class="item-actions">
                                    <label for="quantity">Menge: </label>
                                    <p> {{ item.anzahl }}</p>
                                    <button @click="removeFromCart(item)" style="width: 50px;">Löschen</button>
                                </div>
                            </div>
                            <div class="item-price">
                                <p>{{ (item.preis * item.anzahl).toFixed(2) }} €</p>
                            </div>
                        </div>
                    </div>

                    <!-- hier weitere elemente dann so dies das ananas-->
                </div>

                <!-- Zahlungsbereich -->
                <div class="payment-section">
                    <post-order :cartItems="groupedCartItems" :totalAmount="totalWithFees" @orderPlaced="handleOrderPlaced" />
                    <p>Zwischensumme {{ totalItems }} Arikel: <strong>{{ totalAmount.toFixed(2) }} €</strong></p>
                    <p>Versandkosten: <strong>0.00 €</strong></p>
                    <p>Zusatzkosten: <strong>{{ paymentFee.toFixed(2) }} €</strong></p>
                    <p>Gesamtbetrag: <strong>{{ totalWithFees.toFixed(2) }} €</strong></p>
                </div>
            </div>
        </div>
    </body>
    </html>
</template>

<script>
import { useCartStore } from '@/stores/cart';
import { useCustomerStore } from '@/stores/customer';
import PostOrder from '../components/post_order.vue';
import { computed, ref, onMounted, getCurrentInstance, nextTick } from 'vue';

export default {
    name: 'ShoppingCart',
    components: {
        PostOrder
    },
    setup() {
        const cartStore = useCartStore();
        const customerStore = useCustomerStore();

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

        const selectedPaymentMethod = ref('credit-card');
        const paymentFeePercentage = computed(() => {
            if (selectedPaymentMethod.value === 'credit-card') return 0.03;
            if (selectedPaymentMethod.value === 'paypal') return 0.05;
            if (selectedPaymentMethod.value === 'cash-on-delivery') return 0.10;
            return 0;
        });

        const paymentFee = computed(() => {
            return totalAmount.value * paymentFeePercentage.value;
        });

        const totalWithFees = computed(() => {
            return totalAmount.value + paymentFee.value;
        })

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

        // Warte, bis die Instanz geladen ist und hole die Kunden-ID
        onMounted(async () => {
        const instance = getCurrentInstance();

        if (instance) {
            await nextTick(); // Warte, bis der DOM-Tree vollständig gerendert ist
            console.log("SubTree nach vollständigem Rendering:", instance.subTree);
        } else {
            console.error("Aktuelle Instanz konnte nicht abgerufen werden.");
        }

        customerStore.getCustomerIdFromCookie();

        if (!customerStore.customerId) {
            console.error("Kunden-ID konnte nicht aus dem Cookie gelesen werden.");
        }
        });

        // Callback wenn Bestellung erfolgreich platziert wurde
        const handleOrderPlaced = (responseData) => {
        console.log('Bestellung erfolgreich:', responseData);
        alert('Bestellung erfolgreich aufgegeben!');
        };



        // grid-template-row Berechnung anhand der Anzahl im groupedCartItems
        const gridStyle = computed(() => {
            const rows = groupedCartItems.value.length > 0 ? `repeat(${groupedCartItems.value.length}, 200px)` : '200px';
            return {
                'grid-template-rows': rows
            };
        });

        return {
            groupedCartItems,
            totalItems,
            totalAmount,
            removeFromCart,
            gridStyle,
            updateQuantity,
            paymentFee,
            totalWithFees,
            selectedPaymentMethod,
            handleOrderPlaced
        };
    }
};
</script>

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

.payment-section {
    line-height: 1.5rem;
}
/* Cart Items */
.cart-item {
    display: flex;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #e0e0e0;
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
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
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
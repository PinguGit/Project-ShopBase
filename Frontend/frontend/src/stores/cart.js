// src/stores/cart.js
import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
    state: () => ({
        activ_products_shoppingcart: [] // Array für Produkte im Warenkorb
    }),
    actions: {
        addToCart(product) {
            this.activ_products_shoppingcart.push(product);
        },
        removeFromCart(index) {
            this.activ_products_shoppingcart.splice(index, 1);
        }
    }
});
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
        },
        // Menge eines Produkts im Warenkorb aktualisieren
        updateItemQuantity(index, quantity) {
        // Sicherstellen, dass das Produkt existiert und die Menge >= 1 ist
        if (this.activ_products_shoppingcart[index]) {
            this.activ_products_shoppingcart[index].quantity = Math.max(quantity, 1); // Menge nicht kleiner als 1
        }
      }
    }
});
// src/stores/cart.js
import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
    state: () => ({
        activ_products_shoppingcart: [] // Array für Produkte im Warenkorb
    }),
    actions: {
        addToCart(product) {
            // Check if the product is already in the cart
            const existingProduct = this.activ_products_shoppingcart.find(
                item => item.produkt_id === product.produkt_id
            );

            if (existingProduct) {
                // If found, increase its quantity
                existingProduct.anzahl += 1;
            } else {
                // If not found, add it with an initial quantity of 1
                this.activ_products_shoppingcart.push({ ...product, anzahl: 1 });
            }
        },
        removeFromCart(index) {
            this.activ_products_shoppingcart.splice(index, 1);
        },
        // Menge eines Produkts im Warenkorb aktualisieren
        updateItemQuantity(index, quantity) {
        // Sicherstellen, dass das Produkt existiert und die Menge >= 1 ist
        if (this.activ_products_shoppingcart[index]) {
            this.activ_products_shoppingcart[index].anzahl = Math.max(quantity, 1); // Menge nicht kleiner als 1
        }
        },
        // Warenkorb komplett leeren
        clearCart() {
            this.activ_products_shoppingcart = [];
        }
      }
    }
);


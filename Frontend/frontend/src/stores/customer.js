// src/stores/customer.js
import { defineStore } from 'pinia';

export const useCustomerStore = defineStore('customer', {
    state: () => ({
        customerId: null,
        orders: [],
        host: 'http://127.0.0.1:5000/'
    }),
    actions: {
        // Funktion, um die Kunden-ID aus dem Cookie zu holen
        getCustomerIdFromCookie() {
            const cookies = document.cookie.split("; ");
            const customerCookie = cookies.find(row => row.startsWith("kunden_id="));
            if (customerCookie) {
                this.customerId = customerCookie.split("=")[1];
            } else {
                this.customerId = null;
            }
            return this.customerId;
        },
        // Bestellungen eines Kunden abrufen
        async fetchOrders() {
            if (!this.customerId) {
                this.getCustomerIdFromCookie(); // Stelle sicher, dass customerId gesetzt ist
            }
            if (!this.customerId) {
                console.error("Kunden-ID fehlt.");
                return;
            }
            try {
                const response = await fetch(`${this.host}api/get_orders/${this.customerId}`);
                if (!response.ok) {
                    throw new Error(`HTTP-Error: ${response.status}`);
                }
                const data = await response.json();
                this.orders = data;
            } catch (error) {
                console.error('Fehler beim Abrufen der Bestellungen:', error.message);
            }
        }
    }
});

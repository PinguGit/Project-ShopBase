<template>
    <div id="get_all_orders">

    </div>
</template>

<script>
export default {
    name: 'get_all_orders',
    data() {
        return {
            objects: [],
            customer_id: null, // Initialisierung
            host: 'http://127.0.0.1:5000/',
        };
    },
    mounted() {
        this.customer_id = this.getCustomerIdFromCookie(); // Hole die customer_id vor der API-Anfrage
        if (this.customer_id) {
            this.fetchallobjects();
        } else {
            console.error("Customer ID fehlt.");
        }
    },
    methods: {
        // Funktion, um die customer_id aus einem Cookie zu lesen
        getCustomerIdFromCookie() {
            const cookies = document.cookie.split("; ");
            const customerCookie = cookies.find(row => row.startsWith("kunden_id="));
            if (customerCookie) {
                return customerCookie.split("=")[1];
            }
            return null; // Rückgabe null, falls der Cookie fehlt
        },
        // Funktion, um die Bestellungen abzurufen
        async fetchallobjects() {
            try {
                const response = await fetch(`${this.host}api/get_orders/${this.customer_id}`);
                if (!response.ok) {
                    throw new Error(`HTTP-Error: ${response.status}`);
                }
                const data = await response.json();
                this.objects = data;
                console.log("Bestellungen erfolgreich abgerufen:", this.objects);
            } catch (error) {
                console.error('Fehler beim Abrufen der Bestellungen:', error.message);
            }
        },
    },
};
</script>

<style scoped>
#orders {
    font-family: Arial, sans-serif;
}
</style>

<template>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Product Page</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <get_orders_by_customerid @objectsLoaded="handleObjectsLoaded" />
        <!-- get_all_objects Komponente wird hier eingebunden -->
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
        
            <div class="orders">
                <table v-if="objects.length > 0">
                    <thead>
                        <tr>
                            <th>Bestellnr.</th>
                            <th>Verkäufer</th>
                            <th>Produkt</th>
                            <th>Hersteller</th>
                            <th>Preis</th>
                            <th>Anzahl</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="order in objects" :key="order.bestell_id">
                            <td>{{ order.bestell_id }}</td>
                            <td>{{ order.verkaeufer ? order.verkaeufer.name : 'Unbekannt' }}</td>
                            <td>{{ order.produkt ? order.produkt.name : 'Unbekannt' }}</td>
                            <td>{{ order.produkt ? order.produkt.hersteller : 'Unbekannt' }}</td>
                            <td>{{ order.gesamtpreis }}</td>
                            <td>{{ order.anzahl }}</td>
                        </tr>
                    </tbody>
                </table>
                <div v-else>Noch keine Bestellungen gefunden.</div>
                <h1>Orders</h1>
                <p class="price">Gesamtpreis: ...</p>
                <p class="vendor">Verkäufer: ...</p>
            </div>

        </div>
    </body>
    </html>
</template>
  
<script>
// Importiere die get_orders_by_customerid-Komponente
import get_orders_by_customerid from '@/components/get_orders_by_customerid.vue';

export default {
  components: {
    get_orders_by_customerid
  },
  data() {
    return {
      objects: [],
      orders: [], // Hier werden die Bestellungen gespeichert
      verkaeufer: {}, // Verkäuferdaten
      produkte: {}, // Produktdaten
    };
  },
  mounted() {
    console.log('Komponente gemountet, simuliere das Laden von Objekten');

    // Beispielhafte manuelle Simulation von geladenen Daten
    this.handleObjectsLoaded({
      orders: [
        { bestell_id: 1, verkaeufer_id: 101, produkt_id: 201, anzahl: 3, gesamtpreis: 100 },
        { bestell_id: 2, verkaeufer_id: 102, produkt_id: 202, anzahl: 1, gesamtpreis: 50 }
      ],
      verkaeufer: [
        { verkaeufer_id: 101, name: 'Verkäufer 1' },
        { verkaeufer_id: 102, name: 'Verkäufer 2' }
      ],
      produkte: [
        { produkt_id: 201, name: 'Produkt A', hersteller: 'Hersteller A' },
        { produkt_id: 202, name: 'Produkt B', hersteller: 'Hersteller B' }
      ]
    });
},
  methods: {
    handleObjectsLoaded(objects) {
      // Überprüfe, was du von der Komponente zurückbekommst
      console.log('Objekte empfangen:', objects);

      // Empfange die geladenen Objekte und ordne sie den entsprechenden Variablen zu
      this.orders = objects.orders || []; // Bestell-Daten
      this.verkaeufer = objects.verkaeufer || []; // Verkäufer-Daten
      this.produkte = objects.produkte || []; // Produkt-Daten

      // Logge die geladenen Daten
      console.log('Bestellungen:', this.orders);
      console.log('Verkäufer:', this.verkaeufer);
      console.log('Produkte:', this.produkte);

      // Optional: Verarbeitung der Bestellungen
      this.processOrders();
    },
    processOrders() {
      // Gehe durch die Bestellungen und verknüpfe die entsprechenden Verkäufer und Produkte
      console.log('Verarbeite Bestellungen...');
      this.orders.forEach(order => {
        const verkaeuferId = order.verkaeufer_id;
        const produktId = order.produkt_id;

        // Finde den Verkäufer und das Produkt basierend auf den IDs
        order.verkaeufer = this.verkaeufer.find(v => v.verkaeufer_id === verkaeuferId) || {};
        order.produkt = this.produkte.find(p => p.produkt_id === produktId) || {};

        // Logge, wie das Order-Objekt nach der Verarbeitung aussieht
        console.log('Verarbeitete Bestellung:', order);
      });
    }
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
        "tables tables tables tables";
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

table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border: 2px solid #000;
}
th, td {
    padding: 12px 15px;
    text-align: left;
    border: 1px solid #292929;
}
th {
    background-color: #4CAF50;
    color: white;
}
tr:nth-child(even) {
    background-color: #f2f2f2;
}
tr:hover {
    background-color: #ddd;
}
td {
    font-size: 16px;
}
thead {
    font-size: 18px;
}
</style>
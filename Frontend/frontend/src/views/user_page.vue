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
            
            <div class="profile" @click="handleProfileClick">
                <i class="fa-solid fa-user"> Profil</i>
            </div>

            <router-link style="text-decoration: none; color: black;" to="/shopping-cart">
                <div class="basket">
                    <i class="fas fa-shopping-cart"> Warenkorb</i>
                </div>
            </router-link>
        
            <div class="orders">
                <h1 class="orders_header">Bestellungen</h1>
                <table v-if="orders.length > 0">
                    <thead>
                        <tr>
                            <th>Bestellnr.</th>
                            <th>Produkt</th>
                            <th>Hersteller</th>
                            <th>Preis</th>
                            <th>Anzahl</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(order, index) in orders" :key="index">
                            <td>{{ order.bestellnr }}</td>
                            <td>{{ order.produkt_name }}</td>
                            <td>{{ order.hersteller_name }}</td>
                            <td>{{ order.gesamtpreis }}</td>
                            <td>{{ order.anzahl }}</td>
                        </tr>
                    </tbody>
                </table>
                <div v-else>Noch keine Bestellungen gefunden.</div>
            </div>

        </div>
    </body>
    </html>
</template>
  
<script>
// Importiere die Komponente, um sie in dieser Ansicht zu verwenden
import get_orders_by_customerid from '@/components/get_orders_by_customerid.vue';

export default {
  name: 'user-page',
  components: {
    get_orders_by_customerid, // Registrierung der Komponente
  },
  data() {
    return {
      orders: [] // Speichert die Bestellungsdaten
    };
  },
  methods: {
    // Methode zum Setzen der Bestellungen, wenn sie von der Kindkomponente übergeben werden
    handleObjectsLoaded(objects) {
      this.orders = Object.entries(objects).map(([key, value]) => ({
        bestellnr: key,
        ...value,
      }));
    },

    // Funktion, die beim Klick auf das Profil ausgeführt wird
    handleProfileClick() {
      const ablaufDatum = this.getCookieExpiryDate();
      if (ablaufDatum) {
        const currentDate = new Date();
        const expiryDate = new Date(ablaufDatum);

        // Vergleiche das Ablaufdatum mit der aktuellen Zeit
        if (expiryDate > currentDate) {
          this.$router.push('/user-page');
        } else {
            this.$router.push('/login-page');
        }
      } else {
        console.error("Kein Ablaufdatum im Cookie gefunden");
        this.$router.push('/login-page');
      }
    },

    // Hilfsfunktion zum Abrufen des Ablaufdatums aus dem Cookie
    getCookieExpiryDate() {
      const cookies = document.cookie.split("; ");

      // Suche nach dem Cookie mit dem Ablaufdatum
      const expiryCookie = cookies.find(row => row.startsWith("customer_type_expiry="));

      // Wenn das Ablaufdatum-Cookie existiert, gibt es das Datum zurück
      if (expiryCookie) {
        return expiryCookie.split("=")[1];
      }
      return null;
    },
  },
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

.orders {
    margin-top: 50px;
    grid-area: tables;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.orders_header {
    margin-bottom: 20px;
}

table {
    width: 80%;
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
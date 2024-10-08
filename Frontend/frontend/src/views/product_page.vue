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
        <!-- get_all_objects Komponente wird hier eingebunden -->
        <get_all_objects @objectsLoaded="handleObjectsLoaded" />

        <!-- <p> {{ objects }}</p> -->

        <div class="container">
            <div class="logo">
                <img src="../assets/LogoReal.png" alt="Logo" height="100px" width="125px">
            </div>
            <div class="search-bar">
                <input type="text" placeholder="Search Bar">
            </div>
            <div class="profile">
                <i class="fa-solid fa-user"> Benutzer</i>
            </div>
            <div class="basket">
                <i class="fas fa-shopping-cart"> Shopping Cart</i>
            </div>
            <div class="filter">
                <h4>Filter Products</h4>
                <form id="filter-form">
                    <!-- Filter by Product Name -->
                    <label for="product-name">Product Name:</label>
                    <input type="text" id="product-name" v-model="filters.productName" placeholder="Enter product name">
            
                    <!-- Filter by Price -->
                    <label for="price">Price:</label>
                    <select id="price-filter" v-model="filters.price">
                        <option value="all">All Prices</option>
                        <option value="below">Below 50</option>
                        <option value="between">Between 50 and 100</option>
                        <option value="above">Above 100</option>
                    </select>
                    
                    <!-- Filter by Stock -->
                    <label for="stock">Stock:</label>
                    <select id="stock-filter" v-model="filters.stock">
                        <option value="all">All Stock</option>
                        <option value="below">Below 50</option>
                        <option value="between">Between 50 and 100</option>
                        <option value="above">Above 100</option>
                    </select>
            
                    <!-- Filter by Seller -->
                    <label for="seller">Seller:</label>
                    <input type="text" id="seller" v-model="filters.seller" placeholder="Enter seller">
            
                    <!-- Filter by Delivery Date -->
                    <label for="delivery-date">Delivery Date (yyyy-mm-dd):</label>
                    <input type="date" id="delivery-date" v-model="filters.deliveryDate">
            
                    <button type="button" @click="filterProducts">Apply Filter</button>
                </form>
            </div>
            

            <!-- Product List -->
            <div class="product-list">
                <!-- Product Box -->
                <div v-for="product in products" :key="product.produkt_name" class="product-box">
                    <p>{{ product.produkt_name }} {{ product.preis }}</p>
                </div>
            </div>
        </div>
    </body>
    </html>
</template>
  
<script>
import get_all_objects from '@/components/get_all_objects.vue';

export default {
    name: 'ProductPage',
    components: {
        get_all_objects 
    },
    data() {
        return {
            products: [],
            filters: {
                productName: '',
                price: 'all',
                stock: 'all',
                seller: '',
                deliveryDate: ''
            },
            filteredProducts: []
        };
    },
    methods: {
        handleObjectsLoaded(objects) {
            this.products = objects.product; // Speichere die abgerufenen Produkte
            //this.filteredProducts = objects; // Initialisiere die gefilterten Produkte
            //this.filterProducts(); // Optional: Filter anwenden
        },
        /*filterProducts() {
            this.filteredProducts = this.products.filter(product => {
                const matchesProductName = product.name.toLowerCase().includes(this.filters.productName.toLowerCase());
                const matchesPrice = this.filters.price === 'all' ||
                    (this.filters.price === 'below' && product.price < 50) ||
                    (this.filters.price === 'between' && product.price >= 50 && product.price <= 100) ||
                    (this.filters.price === 'above' && product.price > 100);
                const matchesStock = this.filters.stock === 'all' ||
                    (this.filters.stock === 'below' && product.stock < 50) ||
                    (this.filters.stock === 'between' && product.stock >= 50 && product.stock <= 100) ||
                    (this.filters.stock === 'above' && product.stock > 100);
                const matchesSeller = !this.filters.seller || product.seller.toLowerCase().includes(this.filters.seller.toLowerCase());
                const matchesDeliveryDate = !this.filters.deliveryDate || product.deliveryDate === this.filters.deliveryDate;
                console.log(this.filteredProducts)
                return matchesProductName && matchesPrice && matchesStock && matchesSeller && matchesDeliveryDate;
            });
        }*/
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
    font-family: Arial, sans-serif;
}

.container {
    display: grid;
    grid-template-columns: 200px 1fr 150px 150px;
    grid-template-rows: 100px 1fr;
    grid-template-areas:
        "logo search-bar basket profile"
        "filter product-list product-list product-list";
    gap: 10px;
    height: 100vh;
}

.logo {
    grid-area: logo;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid black;
    background: #2c313d;
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
}

.basket {
    grid-area: basket;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid black;
}

.profile {
    grid-area: profile;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid black;
}

.basket, .profile {
    font-size: 12px;
    margin: 10px;
}

.filter {
    grid-area: filter;
    background-color: #f0f0f0;
    border: 1px solid black;
    padding: 10px;
    margin-top: 10px;
}

.product-list {
    grid-area: product-list;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

/* Product Boxes */
.product-box {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-auto-flow: column;
    align-items: center;
    border: 1px solid black;
    padding: 10px;
    background-color: #f0f0f0;
    width: 100%;
    justify-content: space-between;
}

.image-section {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 150px;
    margin-right: 20px;
}

.image {
    width: 100px;
    height: 100px;
    background-color: #ccc;
    text-align: center;
    line-height: 100px;
}

.info-section {
    display: grid;
    grid-column-start: 2;
    grid-column-end: 7;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(3, 1fr);
    height: 100%;
}

h3 {
    font-size: 18px;
    grid-column: 1 / -1;
}

.price-section {
    display: flex;
    align-items: center;
    grid-row: 2 / 4;
}

.price {
    font-size: 24px;
    font-weight: bold;
}

.seller, .delivery-date {
    font-size: 14px;
}

.seller {
    grid-column: 2 / 4; 
}

.delivery-date {
    grid-column: 2 / 4;
}

.stock {
    grid-column: 4 / 5;
    grid-row: 2 / 4;
}

.actions {
    display: flex;
    gap: 50px;
    grid-row: 2 / 4;
    grid-column: 5 / 7;
    justify-content: center;
}

button {
    padding: 10px;
    width: 200px;
    border: none;
    cursor: pointer;
}

.add-to-basket {
    background-color: #4CAF50;
    color: white;
}

.buy-now {
    background-color: #f44336;
    color: white;
}

</style>
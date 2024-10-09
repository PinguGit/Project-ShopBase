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
                <input type="text" placeholder="Search for products" v-model="filters.productName">
            </div>
            <div class="profile">
                <i class="fa-solid fa-user"> Benutzer</i>
            </div>
            <div class="basket" href="">
                <router-link to="/shopping-cart"><i class="fas fa-shopping-cart"> Shopping Cart</i></router-link>
            </div>
            <div class="filter">
                <h4>Filter Products</h4>
                <form id="filter-form">
                    <!-- Filter by Product Name -->
            
                    <!-- Filter by Price -->
                    <label for="price">Price:</label>
                    <input type="number" id="price-filter" v-model="filters.price">
            
                    <!-- Filter by Seller -->
                    <label for="seller">Seller:</label>
                    <input type="text" id="seller" v-model="filters.seller" placeholder="Enter seller">
            
                </form>
            </div>
        
            <!-- Product List -->

            <div class="product-list">
                <table class="product-table">
                    <thead>
                        <tr>
                            <th>Produkt Name</th>
                            <th>Preis</th>
                            <th>Hersteller</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="product in this.filteredProducts" :key="product.produkt_name">
                            <td>{{ product.produkt_name }}</td>
                            <td>{{ product.preis }}</td>
                            <td>{{ product.hersteller }}</td>
                        </tr>
                    </tbody>
                </table>
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
                price: '',
                stock: 'all',
                seller: '',
                deliveryDate: ''
            },
            filteredProducts: []
        };
    },

    watch: {
        filters: {
            handler() {
                this.filterProducts();
            },
            deep: true
        }
    },
    methods: {
        handleObjectsLoaded(objects) {
            this.products = Object.values(objects.product); 
            this.filterProducts(); 
        },

        filterProducts() {
            if (Array.isArray(this.products)) {
                this.filteredProducts = [];
            }
        


            // filter function from js script if function (after =>) if all consts return true product gets appended to filterdproducts
            this.filteredProducts = this.products.filter(product => {
                const namematch = product.produkt_name.toLowerCase().includes(this.filters.productName.toLowerCase());
                const pricematch = this.filters.price === '' || this.product.preis <= this.filters.price;
                const sellermatch = product.hersteller.toLowerCase().includes(this.filters.seller.toLowerCase());

                return namematch && pricematch && sellermatch;
            }

            )
            console.log("Filterd products")
            console.log(this.filteredProducts)
            }       
        }
    }
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

<style>
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

.product-list {
    grid-area: product-list;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.product-table {
    width: 100%;
    border-collapse: collapse;
}

.product-table th, .product-table td {
    border: 1px solid black;
    padding: 10px;
    text-align: center;
}

.product-table th { 
    background-color: #2c313d;
    color: white;
}

.product-table tr:nth-child(even) {
    background-color: #f0f0f0;
}

.product-table tr:nth-child(odd) {
    background-color: #ffffff;
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
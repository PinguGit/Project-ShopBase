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
            <router-link to="/">
                <div class="logo">
                    <img src="../assets/LogoReal.png" alt="Logo" height="100px" width="125px">
                </div>
            </router-link>
            <div class="search-bar">
                <input type="text" placeholder="Suche nach Produkten..." v-model="filters.productName">
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
                <div class="product" v-for="product in this.filteredProducts" :key="product.produkt_name">
                    <div class="product-image">
                        <img src="../assets/logo.png" alt="Produkt Bild">
                    </div>
                    <h3 class="product-title">{{ product.produkt_name }}</h3>
                    <p class="product-price">Preis: {{ product.preis }}€</p>
                    <p class="product-vendor">Verkäufer: {{ product.verkaeufer[0].verkaeufer_name }}</p>
                    <p class="product-producer">Hersteller: {{ product.hersteller }}</p>
                    <button class="add-to-cart" @click="addtoshoppingcart(product)"> In den Warenkorb hinzufügen</button>
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
                price: '',
                stock: 'all',
                seller: '',
                deliveryDate: ''
            },
            filteredProducts: [],
            activ_products_shoppingcart: [],
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
            },
        
        addtoshoppingcart(product) {
            this.activ_products_shoppingcart.push(product);
            console.log('shoppingcart');
            console.log(this.activ_products_shoppingcart)
        },
        
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
        "filter product-list product-list product-list";
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

.filter {
    grid-area: filter;
    background-color: #fff;
    border-radius: 10px;
    border: 1px solid #6c757d;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 15px;
}

.filter h4 {
    margin-bottom: 15px;
    color: #007bff;
}

.filter input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border-radius: 5px;
    border: 1px solid #ced4da;
    background-color: #f8f9fa;
}

.search-bar input:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}


.product-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    width: 100%;
    box-sizing: border-box;
}

.product {
    display: grid;
    grid-template-columns: 1fr 2fr 2fr 1fr;
    grid-template-rows: auto auto;
    gap: 15px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 15px;
    align-items: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    width: 100%;
}

.product:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.product-image {
    grid-column: 1 / 2;
    grid-row: 1 / -1;
    display: flex;  /* Flexbox verwenden */
    justify-content: center;  /* Zentriert horizontal */
    align-items: center;  /* Zentriert vertikal */
}

.product-image img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
}

.product-title {
    grid-column: 2 / 4;
    font-size: 1.2rem;
    color: #343a40;
}

.product-price {
    grid-column: 2 / 3;
    font-size: 1rem;
    color: #007bff;
}

.product-producer {
    grid-column: 3 / 4;
    font-size: 0.9rem;
    color: #6c757d;
}

.add-to-cart {
    grid-column: 4 / 5;
    grid-row: 1 / -1;
    display: flex;  /* Flexbox verwenden */
    justify-content: center;  /* Zentriert horizontal */
    align-items: center;  /* Zentriert vertikal */
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    justify-self: center;
}

.add-to-cart:hover {
    background-color: #0056b3;
    transform: scale(1.05);
}



</style>
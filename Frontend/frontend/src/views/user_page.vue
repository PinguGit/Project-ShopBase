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
        
            <!-- User shit dann -->

        </div>
    </body>
    </html>
</template>
  
<script>
</script>

<style scoped>
</style>
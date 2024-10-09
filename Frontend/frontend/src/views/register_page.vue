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
        <div class="register-container">
            <h2>Register</h2>
            <form>
                <div class="input-container">
                    <i class="fas fa-user"></i>
                    <input type="text" placeholder="Vorname" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-user"></i>
                    <input type="text" placeholder="Nachname" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-home"></i>
                    <input type="text" placeholder="Strasse" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-home"></i>
                    <input type="text" placeholder="Hausnummer" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-envelope"></i>
                    <input type="email" placeholder="Email" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-map-marker-alt"></i>
                    <input type="text" placeholder="PLZ" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-globe"></i>
                    <select required>
                        <option value="" disabled selected>Land auswählen</option>
                        <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
                    </select>
                </div>
                <div class="input-container">
                    <i class="fas fa-lock"></i>
                    <input type="password" placeholder="Passwort" required>
                </div>
                <div class="input-container">
                    <i class="fas fa-calendar-alt"></i>
                    <input type="date" placeholder="Geburtsdatum" required>
                </div>
                <button type="submit"><i class="fas fa-user-plus"></i> Register</button>
                <router-link to="/login-page"><p class="back-to-login">Zurück zum Login</p></router-link>
            </form>
        </div>
    </body>
    </html>
</template>
  
<script>
export default {
  name: "RegisterPage",
  data() {
    return {
      countries: [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", 
        "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", 
        "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", 
        "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", 
        "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", 
        "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", 
        "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", 
        "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", 
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", 
        "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", 
        "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", 
        "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", 
        "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", 
        "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", 
        "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
        "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
        "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
        "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", 
        "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", 
        "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", 
        "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", 
        "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
        "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
        "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", 
        "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", 
        "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", 
        "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", 
        "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", 
        "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", 
        "United Kingdom", "USA", "Uruguay", "Uzbekistan", 
        "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
      ]
    }
  }
}
</script>

<style scoped>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
    }

    .register-container {
        background-color: #fff;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        width: 400px;
        text-align: center;
    }

    h2 {
        margin-bottom: 20px;
    }

    .input-container {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }

    .input-container i {
        margin-right: 10px;
        color: #007bff;
    }

    input[type="text"], input[type="email"], input[type="password"], input[type="date"] {
        width: 90%;
        padding: 10px;
        margin: 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    button {
        width: 100%;
        padding: 10px;
        background-color: #28a745;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
    }

    button:hover {
        background-color: #218838;
    }

    select {
        width: 100%;
        padding: 10px;
        margin: 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .input-container select {
        padding-right: 30px; /* Adds padding to make room for the arrow */
    }
</style>
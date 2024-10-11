<template>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Product Page</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body id=register_page>
        <div class="register-container">
        <h2>Register</h2>
    
        <div class="custom-radio">
            <div class="radio-item">
            <input type="radio" id="private" value="private" v-model="form.customerType" style="margin-bottom: 5px;">
            <label for="private">Privatkunde</label>
            </div>
            
            <div class="radio-item">
            <input type="radio" id="business" value="business" v-model="form.customerType" style="margin-bottom: 5px;">
            <label for="business">Händler</label>
            </div>
        </div>
    
        <!-- Form Submission Handler -->
        <form @submit.prevent="register">
            <div class="input-container">
            <i class="fas fa-user"></i>
            <input type="text" v-model="form.firstName" :placeholder="form.customerType === 'business' ? 'Geschäftsname' : 'Vorname'" required>
            </div>
            <div v-if="form.customerType !== 'business'" class="input-container">
            <i class="fas fa-user"></i>
            <input type="text" v-model="form.lastName" placeholder="Nachname" required>
            </div>
            <div class="form-container">
            <div class="form-row">
                <div class="input-container">
                <i class="fas fa-home"></i>
                <input type="text" v-model="form.street" placeholder="Straße" required>
                </div>
                <div class="input-container">
                <i class="fas fa-home"></i>
                <input type="text" v-model="form.houseNumber" placeholder="Hausnummer" required>
                </div>
            </div>
            </div>
            
            <div class="input-container">
            <i class="fa-regular fa-building"></i>
            <input type="text" v-model="form.city" placeholder="Stadt" required>
            </div>

            <div class="input-container">
            <i class="fa-solid fa-location-dot"></i>
            <input type="text" v-model="form.zipCode" placeholder="PLZ" required>
            </div>

            <div class="input-container">
            <i class="fas fa-envelope"></i>
            <input type="email" v-model="form.email" placeholder="Email" required>
            </div>

            <div class="input-container">
            <i class="fas fa-globe"></i>

            
            <select v-model="form.countryId" required>
                <option value="" disabled selected>Land auswählen</option>
                <option v-for="country in countries" :key="country.id" :value="country.id">{{ country.name }}</option>
            </select>
            </div>

            <div class="input-container">
            <i class="fas fa-lock"></i>
            <input type="password" v-model="form.password" placeholder="Passwort" required>
            </div>

            <div class="input-container">
            <i class="fas fa-calendar-alt"></i>
            <input type="date" v-model="form.birthDate" placeholder="Geburtsdatum" required>
            </div>
            
            <!-- Submit Button triggers the post_register_user component -->
            <button type="submit">
            <i class="fas fa-user-plus"></i> Register
            </button>
            <router-link to="/login-page">
            <p class="back-to-login">Zurück zum Login</p>
            </router-link>
            
            <!-- Set reference to the function to call it in methods -->
            <post_register_user ref="postRegisterComponent" :form="form" @response="handleResponse"/>
        </form>
        </div>
    </body>
</template>
  
  <script>
  import post_register_user from '../components/post_register_user.vue';
  
  export default {
    name: "RegisterPage",
    components: {
      post_register_user
    },
    data() {
      return {
        form: {
          firstName: '',
          lastName: '',
          street: '',
          houseNumber: '',
          email: '',
          zipCode: '',
          countryId: '2',
          password: '',
          birthDate: '',
          city: '',
          customerType: ''
        },
        countries: [
        { id: 1, name: "Germany" },
        { id: 2, name: "USA" },
        { id: 3, name: "France" },
        { id: 4, name: "Andorra" },
        { id: 5, name: "Angola" },
        { id: 6, name: "Antigua and Barbuda" },
        { id: 7, name: "Argentina" },
        { id: 8, name: "Armenia" },
        { id: 9, name: "Australia" },
        { id: 10, name: "Austria" },
        { id: 11, name: "Azerbaijan" },
        { id: 12, name: "Bahamas" },
        { id: 13, name: "Bahrain" },
        { id: 14, name: "Bangladesh" },
        { id: 15, name: "Barbados" },
        { id: 16, name: "Belarus" },
        { id: 17, name: "Belgium" },
        { id: 18, name: "Belize" },
        { id: 19, name: "Benin" },
        { id: 20, name: "Bhutan" },
        { id: 21, name: "Bolivia" },
        { id: 22, name: "Bosnia and Herzegovina" },
        { id: 23, name: "Botswana" },
        { id: 24, name: "Brazil" },
        { id: 25, name: "Brunei" },
        { id: 26, name: "Bulgaria" },
        { id: 27, name: "Burkina Faso" },
        { id: 28, name: "Burundi" },
        { id: 29, name: "Cabo Verde" },
        { id: 30, name: "Cambodia" },
        { id: 31, name: "Cameroon" },
        { id: 32, name: "Canada" },
        { id: 33, name: "Central African Republic" },
        { id: 34, name: "Chad" },
        { id: 35, name: "Chile" },
        { id: 36, name: "China" },
        { id: 37, name: "Colombia" },
        { id: 38, name: "Comoros" },
        { id: 39, name: "Congo (Congo-Brazzaville)" },
        { id: 40, name: "Costa Rica" },
        { id: 41, name: "Croatia" },
        { id: 42, name: "Cuba" },
        { id: 43, name: "Cyprus" },
        { id: 44, name: "Czech Republic" },
        { id: 45, name: "Denmark" },
        { id: 46, name: "Djibouti" },
        { id: 47, name: "Dominica" },
        { id: 48, name: "Dominican Republic" },
        { id: 49, name: "Ecuador" },
        { id: 50, name: "Egypt" },
        { id: 51, name: "El Salvador" },
        { id: 52, name: "Equatorial Guinea" },
        { id: 53, name: "Eritrea" },
        { id: 54, name: "Estonia" },
        { id: 55, name: "Eswatini" },
        { id: 56, name: "Ethiopia" },
        { id: 57, name: "Fiji" },
        { id: 58, name: "Finland" },
        { id: 59, name: "Algeria" },
        { id: 60, name: "Gabon" },
        { id: 61, name: "Gambia" },
        { id: 62, name: "Georgia" },
        { id: 63, name: "Afghanistan" },
        { id: 64, name: "Ghana" },
        { id: 65, name: "Greece" },
        { id: 66, name: "Grenada" },
        { id: 67, name: "Guatemala" },
        { id: 68, name: "Guinea" },
        { id: 69, name: "Guinea-Bissau" },
        { id: 70, name: "Guyana" },
        { id: 71, name: "Haiti" },
        { id: 72, name: "Honduras" },
        { id: 73, name: "Hungary" },
        { id: 74, name: "Iceland" },
        { id: 75, name: "India" },
        { id: 76, name: "Indonesia" },
        { id: 77, name: "Iran" },
        { id: 78, name: "Iraq" },
        { id: 79, name: "Ireland" },
        { id: 80, name: "Israel" },
        { id: 81, name: "Italy" },
        { id: 82, name: "Jamaica" },
        { id: 83, name: "Japan" },
        { id: 84, name: "Jordan" },
        { id: 85, name: "Kazakhstan" },
        { id: 86, name: "Kenya" },
        { id: 87, name: "Kiribati" },
        { id: 88, name: "Kuwait" },
        { id: 89, name: "Kyrgyzstan" },
        { id: 90, name: "Laos" },
        { id: 91, name: "Latvia" },
        { id: 92, name: "Lebanon" },
        { id: 93, name: "Lesotho" },
        { id: 94, name: "Liberia" },
        { id: 95, name: "Libya" },
        { id: 96, name: "Liechtenstein" },
        { id: 97, name: "Lithuania" },
        { id: 98, name: "Luxembourg" },
        { id: 99, name: "Madagascar" },
        { id: 100, name: "Malawi" },
        { id: 101, name: "Malaysia" },
        { id: 102, name: "Maldives" },
        { id: 103, name: "Mali" },
        { id: 104, name: "Malta" },
        { id: 105, name: "Marshall Islands" },
        { id: 106, name: "Mauritania" },
        { id: 107, name: "Mauritius" },
        { id: 108, name: "Mexico" },
        { id: 109, name: "Micronesia" },
        { id: 110, name: "Moldova" },
        { id: 111, name: "Monaco" },
        { id: 112, name: "Mongolia" },
        { id: 113, name: "Montenegro" },
        { id: 114, name: "Morocco" },
        { id: 115, name: "Mozambique" },
        { id: 116, name: "Myanmar" },
        { id: 117, name: "Namibia" },
        { id: 118, name: "Nauru" },
        { id: 119, name: "Nepal" },
        { id: 120, name: "Netherlands" },
        { id: 121, name: "New Zealand" },
        { id: 122, name: "Nicaragua" },
        { id: 123, name: "Niger" },
        { id: 124, name: "Nigeria" },
        { id: 125, name: "North Korea" },
        { id: 126, name: "North Macedonia" },
        { id: 127, name: "Norway" },
        { id: 128, name: "Oman" },
        { id: 129, name: "Pakistan" },
        { id: 130, name: "Palau" },
        { id: 131, name: "Panama" },
        { id: 132, name: "Papua New Guinea" },
        { id: 133, name: "Paraguay" },
        { id: 134, name: "Peru" },
        { id: 135, name: "Philippines" },
        { id: 136, name: "Poland" },
        { id: 137, name: "Portugal" },
        { id: 138, name: "Qatar" },
        { id: 139, name: "Romania" },
        { id: 140, name: "Russia" },
        { id: 141, name: "Rwanda" },
        { id: 142, name: "Saint Kitts and Nevis" },
        { id: 143, name: "Saint Lucia" },
        { id: 144, name: "Saint Vincent and the Grenadines" },
        { id: 145, name: "Samoa" },
        { id: 146, name: "San Marino" },
        { id: 147, name: "Sao Tome and Principe" },
        { id: 148, name: "Saudi Arabia" },
        { id: 149, name: "Senegal" },
        { id: 150, name: "Serbia" },
        { id: 151, name: "Seychelles" },
        { id: 152, name: "Sierra Leone" },
        { id: 153, name: "Singapore" },
        { id: 154, name: "Slovakia" },
        { id: 155, name: "Slovenia" },
        { id: 156, name: "Solomon Islands" },
        { id: 157, name: "Somalia" },
        { id: 158, name: "South Africa" },
        { id: 159, name: "South Korea" },
        { id: 160, name: "South Sudan" },
        { id: 161, name: "Spain" },
        { id: 162, name: "Sri Lanka" },
        { id: 163, name: "Sudan" },
        { id: 164, name: "Suriname" },
        { id: 165, name: "Sweden" },
        { id: 166, name: "Switzerland" },
        { id: 167, name: "Syria" },
        { id: 168, name: "Taiwan" },
        { id: 169, name: "Tajikistan" },
        { id: 170, name: "Tanzania" },
        { id: 171, name: "Thailand" },
        { id: 172, name: "Timor-Leste" },
        { id: 173, name: "Togo" },
        { id: 174, name: "Tonga" },
        { id: 175, name: "Trinidad and Tobago" },
        { id: 176, name: "Tunisia" },
        { id: 177, name: "Turkey" },
        { id: 178, name: "Turkmenistan" },
        { id: 179, name: "Tuvalu" },
        { id: 180, name: "Uganda" },
        { id: 181, name: "Ukraine" },
        { id: 182, name: "United Arab Emirates" },
        { id: 183, name: "United Kingdom" },
        { id: 184, name: "Albania" },
        { id: 185, name: "Uruguay" },
        { id: 186, name: "Uzbekistan" },
        { id: 187, name: "Vanuatu" },
        { id: 188, name: "Vatican City" },
        { id: 189, name: "Venezuela" },
        { id: 190, name: "Vietnam" },
        { id: 191, name: "Yemen" },
        { id: 192, name: "Zambia" },
        { id: 193, name: "Zimbabwe" }
        ],
      };
    },
    methods: {
    register() {
     
      this.$refs.postRegisterComponent.post_register_user();
    },
    handleResponse() {
        if (response.success === true) {
            alert("Login successfull")
        }
        else if (response.success && response.sucess.error) {
            alert("User already exists")
        }
        else {
            alert("Failure by regestration")
        }
    }
    }
  };
  </script>

<style>
#register_page {
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
 
input[type="text"],
input[type="email"],
input[type="password"],
input[type="date"] {
    width: 100%;
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
    padding-right: 30px;
}
 
.form-container {
    display: flex;
    flex-direction: column;
}
 
.form-row {
    display: grid;
    grid-template-columns: 62.5% 35%;
    gap: 10px;
}
 
.hidden {
    display: none;
}
 
/* Radio Button Container */
.custom-radio {
    display: flex;
    flex-direction: row;
    margin-bottom: 5px;
    margin-left: 60px;
}
 
/* Radio Button Item */
.radio-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
 
/* Radio Button Styling */
.radio-item label {
    position: relative;
    padding-left: 15px;
    padding-right: 25px;
}
 
/* Anpassungen für die Radio-Buttons */
.radio-item input[type="radio"] {
    width: 20px;
    height: 20px;
    margin-left: 15px;
    align-self: center;
    appearance: none;
    border: 2px solid #007bff;
    border-radius: 50%;
    cursor: pointer;
}
 
/* Styling für den aktivierten Zustand */
.radio-item input[type="radio"]:checked {
    background-color: #007bff;
    border: 2px solid #0056b3;
}

</style>
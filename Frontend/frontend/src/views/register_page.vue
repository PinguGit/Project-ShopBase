<template>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Product Page</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    </head>
    <body>
        <div class="register-container">
        <h2>Register</h2>
    
        <div class="custom-radio">
            <div class="radio-item">
            <input type="radio" id="private" value="private" v-model="customerType" style="margin-bottom: 5px;">
            <label for="private">Privatkunde</label>
            </div>
    
            <div class="radio-item">
            <input type="radio" id="business" value="business" v-model="customerType" style="margin-bottom: 5px;">
            <label for="business">Händler</label>
            </div>
        </div>
    
        <!-- Form Submission Handler -->
        <form>
            <div class="input-container">
            <i class="fas fa-user"></i>
            <input type="text" v-model="form.firstName" :placeholder="customerType === 'business' ? 'Geschäftsname' : 'Vorname'" required>
            </div>
            <div v-if="customerType !== 'business'" class="input-container">
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
            
            <post_register_user @registration-success="handleRegistrationSuccess" />
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
          countryId: '',
          password: '',
          birthDate: ''
        },
        countries: [
          { id: 1, name: "Germany" },
          { id: 2, name: "USA" },
          // Add other countries as necessary...
        ],
        customerType: '' // Storing customer type (private or business)
      };
    },
    methods: {
      register() {
        this.$refs.postRegisterComponent.post_register_user(this.form);
      }
    }
  };
  </script>

<style>
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
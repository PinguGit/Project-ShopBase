<template>
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
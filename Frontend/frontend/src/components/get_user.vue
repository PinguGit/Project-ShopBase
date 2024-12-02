<template>
    <p>{{loge()}}</p>
    
</template>
  
<script>
 export default {
  data() {
    return {
      host: 'http://127.0.0.1:5000/',
    };
  },
  props: {
    user_id: {
        type: [Number],
        default: null,
    },
    customer_type: {
        type: String,
        default: "",
    },
},
  name: "get_user",

methods: {
    loge() {
        console.log(this.user_id, this.customer_type)
    },
    async fetchuser() {
        try {
          const response = await fetch(`${this.host}api/get_object/""/${this.objectid}`);
          const data = await response.json(); 

          this.objects = data
        
        } catch (error) {
          console.error(`Fehler beim Abrufen der Daten für Tabelle ${this.tablename} und ID ${this.objectid}:`, error);
        }
      }
    }
  }
</script>
  
  <style scoped>
  /* Dein CSS hier */
  </style>
<template>
    <div id="get_all_object">
    </div>
  </template>
  
  <script>
 export default {
  name: 'get_all_object',
  data() {
    return {
      objects: {}, 
      tablename: '',
      objectid: '', 
      host: 'http://127.0.0.1:5000/',
    };
  },
  mounted() {
    this.fetchallobjects(); 
  },
  methods: {
    async fetchallobjects() {
        try {
          const response = await fetch(`${this.host}api/get_object/${this.tablename}/${this.objectid}`);
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
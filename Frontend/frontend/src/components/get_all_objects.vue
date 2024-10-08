<template>
    <div id="get_all_objects">
      <h1>Objekte</h1>
      <ul>
        <li v-for="(object, index) in objects" :key="index">{{ object }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'get_all_objects',
    data() {
      return {
        objects: [], // Array, um die abgerufenen Objekte zu speichern
        tableName: 'product',  // Beispiel-Tabellenname, kann dynamisch geändert werden
        host: 'http://127.0.0.1:5000/',
        
    
    };
    },
    mounted() {
      this.fetchallobjects(this.tableName); // Beim Laden der Komponente werden die Objekte abgerufen
    },
    methods: {
      fetchallobjects(tableName) {
        fetch(`${this.host}api/get_all_objects/${tableName}`)
          .then(response => response.json()) // Konvertiere die Antwort in JSON
          .then(data => {
            this.objects = data; // Speichere die abgerufenen Objekte im Array
          })
          .catch(error => {
            console.error("Fehler beim Abrufen der Objekte:", error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Dein CSS hier */
  </style>
<template>
    <div id="get_all_objects">
      <h1>Objekte</h1>
      <ul>
        <li v-for="(object, index) in objects" :key="index">{{ object.name }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'get_all_objects',
    data() {
      return {
        objects: [], // Array, um die abgerufenen Objekte zu speichern
        tableName: 'products',
        adress: 'http://localhost:5000' // Beispiel-Tabellenname, kann dynamisch geändert werden
      };
    },
    mounted() {
      this.fetchallobjects(this.tableName); // Beim Laden der Komponente werden die Objekte abgerufen
    },
    methods: {
      fetchallobjects(tablename) {
        fetch(this.adress+`/api/get_all_products/${tablename}`)
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
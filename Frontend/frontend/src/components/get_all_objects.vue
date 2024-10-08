<template>
    <div id="get_all_objects">
    </div>
  </template>
  
  <script>
 export default {
  data() {
    return {
      objects: {}, 
      tableNames: ['kunde', 'orte', 'laender', 'hersteller', 'bestellung', 'passwort', 'product', 'verkaeufer'], 
      host: 'http://127.0.0.1:5000/',
    };
  },
  mounted() {
    this.fetchallobjects(); 
  },
  methods: {
    async fetchallobjects() {

      for (const tableName of this.tableNames) {
        try {
          const response = await fetch(`${this.host}api/get_all_objects/${tableName}`);
          const data = await response.json(); 

          this.objects[tableName] = data

        } catch (error) {
          console.error(`Fehler beim Abrufen der Daten für Tabelle ${tableName}:`, error);
        }
      }
    this.$emit('objectsLoaded', this.objects); // Emitiere die geladenen Objekte
    console.log(this.objects)
    }
  }
};
  </script>
  
  <style scoped>
  /* Dein CSS hier */
  </style>
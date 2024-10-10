<template>
    <div id="get_all_orders">
        <p> test </p>
    </div>


</template>

<script>
export default {
name: 'get_all_orders',
    data() {
        return {
            objects: [],
            customer_id: '1',
            host: 'http://127.0.0.1:5000/',
        };
    },
    mounted() {
    this.fetchallobjects();
    },
    methods: {
        async fetchallobjects() {
         try {
            const response = await fetch (`${this.host}api/get_orders/${this.customer_id}`)
            const data = await response.json();

            this.objects = data
         } catch(error) {
            console.error('Fehler beim Abrufen der Daten für Tabell');
         }   
            
        }
    }

}
</script>
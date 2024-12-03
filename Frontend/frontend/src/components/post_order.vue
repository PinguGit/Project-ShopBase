<template>
  <div>
    <!-- Button zum Abschicken der Bestellung -->
    <button @click="handleCheckout">Bestellung abschicken</button>
  </div>
</template>

<script>
import { useCustomerStore } from '@/stores/customer';

export default {
  name: 'PostOrder',
  props: {
    cartItems: Array,  // Warenkorbartikel
    totalAmount: Number // Gesamtbetrag inkl. Gebühren
  },
  setup(props, { emit }) {
    const customerStore = useCustomerStore();

    const handleCheckout = async () => {
      try {
        const customerId = customerStore.customerId;

        // Produkte mit den nötigen Daten vorbereiten
        const products = props.cartItems.map(item => ({
          produkt_id: item.produkt_id,
          anzahl: item.quantity,
          gesamtbetrag: props.totalAmount.toFixed(2),
        }));

        console.log('Request Body:', products);

        // Fetch-Aufruf
        const response = await fetch(`http://127.0.0.1:5000/api/create_bestellung/${customerId}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json', // Header korrekt setzen
          },
          body: JSON.stringify({
            products: [
              { produkt_id: 1, anzahl: 2, gesamtpreis: '19.99' }
            ],
          }),
        });

        console.log("Response:", response);

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Fehler beim Absenden der Bestellung.');
        }

        // Erfolgshandling
        const responseData = await response.json();
        emit('orderPlaced', responseData);
      } catch (error) {
        console.error('Fehler:', error.message);
        emit('orderError', error.message);
      }
    };

    return {
      handleCheckout
    };
  }
};
</script>


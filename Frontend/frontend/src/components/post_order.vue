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
    cartItems: Array,  // Warenkorbartikel, die an die Komponente übergeben werden
    totalAmount: Number // Gesamtbetrag mit Gebühren
  },
  setup(props, { emit }) {
    const customerStore = useCustomerStore();

    const handleCheckout = async () => {
      try {
        const customerId = customerStore.customerId;

        if (!customerId) {
          throw new Error('Kunden-ID nicht gefunden.');
        }

        // Bereite die Produktdaten vor
        const products = props.cartItems.map(item => ({
          produkt_id: item.produkt_id,
          anzahl: item.anzahl,
          gesamtpreis: (item.preis * item.anzahl).toFixed(2)
        }));

        // Sende Bestellung an das Backend
        const response = await fetch(`http://localhost:5000/create_bestellung/${customerId}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ products })
        });

        const responseData = await response.json();

        if (response.ok && responseData.success) {
          console.log('Bestellungen erstellt:', responseData.bestell_ids);
          emit('orderPlaced', responseData); // Bestell-ID an die Eltern-Komponente weitergeben
        } else {
          throw new Error('Fehler bei der Bestellung.');
        }
      } catch (error) {
        console.error('Fehler:', error);
        alert('Es gab ein Problem bei der Bestellung.');
      }
    };

    return {
      handleCheckout
    };
  }
};
</script>

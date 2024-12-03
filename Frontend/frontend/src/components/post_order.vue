<template>
  <div>
    <!-- Button zum Abschicken der Bestellung -->
    <button @click="handleCheckout" class="buy-button">Bestellung abschicken</button>
  </div>
</template>

<script>
import { useCartStore } from '@/stores/cart';
import { useCustomerStore } from '@/stores/customer';
import { useRouter } from 'vue-router';

export default {
  name: 'PostOrder',
  props: {
    cartItems: Array,  // Warenkorbartikel
    totalAmount: Number // Gesamtbetrag inkl. Gebühren
  },
  setup(props, { emit }) {
    const customerStore = useCustomerStore();
    const router = useRouter();
    const cartStore = useCartStore();

    const handleCheckout = async () => {
      try {
        const customerId = customerStore.customerId;

        // Produkte mit den nötigen Daten vorbereiten
        const products = props.cartItems.map(item => ({
          produkt_id: item.produkt_id,
          anzahl: item.quantity,
          gesamtpreis: props.totalAmount.toFixed(2),
        }));

        const requestBody = {
          products: products,
        };

        // Fetch-Aufruf
        const response = await fetch(`http://127.0.0.1:5000/api/create_bestellung/${customerId}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json', // Header korrekt setzen
          },
          body: JSON.stringify(requestBody),
        });


        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Fehler beim Absenden der Bestellung.');
        }

        // Erfolgshandling
        const responseData = await response.json();
        emit('orderPlaced', responseData);

        // Warenkorb leeren
        cartStore.clearCart();

        // Weiterleitung zur Startseite
        router.push('/');
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

<style>
.buy-button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #ffffff;
    border: none;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    margin-bottom: 15px;
}

.buy-button:hover {
    background-color: #0053ac;
}
</style>


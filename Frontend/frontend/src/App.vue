<template>
  <div id="app">
    <!-- Navigation -->
    <nav>
      <router-link to="/">Product Page</router-link>
      <router-link to="/api_test">API Test Page</router-link>
    </nav>

    <!-- Router View für dynamische Komponenten basierend auf der Route -->
    <router-view></router-view>
  </div>
</template>

<script>
// Falls du get_all_objects direkt einbinden möchtest:
// import get_all_objects from './components/get_all_objects.vue';

export default {
  name: 'App',
  components: {
    // Falls du get_all_objects direkt verwenden möchtest:
    // get_all_objects,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  margin-bottom: 20px;
}

router-link {
  margin-right: 10px;
}
</style>
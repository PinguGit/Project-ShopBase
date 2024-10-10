<template>
  <div id="app">
    <!-- Navigation -->
    <nav>

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
  margin-top: 0px;
}

nav {
  margin-bottom: 0px;
}

router-link {
  margin-right: 10px;
}
</style>
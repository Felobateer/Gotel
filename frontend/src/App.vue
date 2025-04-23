<script setup>
import Nav from './components/navbar/nav.vue'
import Footer from './components/footer/footer.vue'
import router from './router'
</script>

<template>
  <Nav></Nav>
  <router-view></router-view>
  <Footer></Footer>
</template>

<style scoped>
</style>

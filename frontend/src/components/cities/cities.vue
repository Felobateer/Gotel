<script setup>
import CityCard from './citycard.vue'
import popularJson from './cities.json'
import { ref } from 'vue'

const populars = ref(popularJson.popular)


</script>

<template>
  <section>
    <h1 class="text-white fs-1 my-5 text-center">Popular searches</h1>
    <div id="cityCards">
      <CityCard v-for="popular in populars" :key="popular.id" :popular="popular" />
    </div>
  </section>
</template>

<style scoped>
#cityCards {
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 15px;
}

@media (max-width: 1000px) {
  #cityCards {
    grid-template-columns: repeat(2, 1fr);
  }

  #cityCard {
    margin: 1rem 0;
  }
}

@media (max-width: 500px) {
  #cityCards {
    width: 100%;
  }
}
</style>
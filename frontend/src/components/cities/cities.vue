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

#cityCard {
  width: fit-content;
  padding: 15px;
  background-color: #0c111a;
  border-radius: 15px;
}

#cityCard p {
  background: none;
}

#cityCard #button {
  width: 100%;
}

#cityImg {
  width: 18rem;
  height: 21rem;
  margin-bottom: 1rem;
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

  #cityCard p {
    font-size: 10px;
  }

  #cityImg {
    width: 9rem;
    height: 10.5rem;
    margin-bottom: 0.5rem;
  }
}
</style>
<script setup>
import { computed } from 'vue'

const props = defineProps({
  popular: {
    type: Object,
    required: true
  }
})

const imageUrl = computed(() =>
  new URL(`${props.popular.img}`, import.meta.url).href
)
</script>

<template>
  <div id="cityCard">
    <img :src="imageUrl" id="cityImg" alt="City Image" />
    <p class="text-white text-start py-0 px-3 lh-1">{{ popular.city }}</p>
    <p class="text-white text-start py-0 px-3 lh-1">{{ popular.hotels }} Hotels</p>
    <p class="text-white text-start py-0 px-3 lh-1">On average € {{ popular.average }}</p>
  </div>
</template>

<style scoped>
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

@media (max-width: 500px) {
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
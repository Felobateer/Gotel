<script setup>
import { defineProps } from 'vue'
import { RouterLink } from 'vue-router'

defineProps({
  popular: {
    type: Object,
    required: true
  }
})
</script>

<template>
    <div id="cityCard">
      <img :src="popular.img" id="cityImg" />
      <p class="text-white text-start py-0 px-3 lh-1">{{ popular.city }}</p>
      <p class="text-white text-start py-0 px-3 lh-1">{{ popular.hotels }} Hotels</p>
      <p class="text-white text-start py-0 px-3 lh-1">On average € {{ popular.average }}</p>
      <RouterLink id="button" class="btn btn-warning" to="/Book">Book</RouterLink>
    </div>
  </template>



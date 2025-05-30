<script setup>
import { onMounted, defineComponent } from 'vue'
import * as bootstrap from 'bootstrap'

onMounted(() => {
  new bootstrap.Offcanvas(document.getElementById('offcanvasRight'))
})

defineProps({
  links: {
    type: Array,
    required: true
  }
})
</script>

<template>
    <button class="btn" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
        <i class="fa-solid fa-bars"></i>
    </button>
  
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasRightLabel">
            <img  src="/Gotel-logo-fedbbdcb.jpg" alt="Gotel" class="logo"/>
        </h5>
      </div>
      <div class="offcanvas-body">
        <ul>
        <li v-for="(link, index) in links" :key="index">
          <router-link :to="link.path" class="nav-link">
            {{ link.name }}
          </router-link>
        </li>
      </ul>
      </div>
    </div>
  </template>

<style scoped>
  @import '../../style.css';

    button {
        color: var(--light);
        border: 1px solid white;
    }

    #offcanvasRight {
        background-color: var(--dark);
    }

    ul {
        list-style: none;
        padding: 0;
        display: flex;
        flex-direction: column;
    }

    li {
        margin: 1rem auto;
        font-size: 1rem;
        font: var(--font-b);
        cursor: pointer;
        :hover {
            box-shadow: inset 0 -1px 0 var(--gold);
            color: var(--gold);
            transition: 0.3s;
        }
    }
</style>
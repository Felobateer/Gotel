<script setup>
import { onMounted } from 'vue'
import * as bootstrap from 'bootstrap'

onMounted(() => {
  new bootstrap.Offcanvas(document.getElementById('offcanvasRight'))
})
</script>

<template>
    <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
        <i class="fa-solid fa-bars"></i>
    </button>
  
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasRightLabel">
            <img  src="../../assets/Gotel-logo-fedbbdcb.jpg" alt="Gotel" class="logo"/>
        </h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">
        ...
      </div>
    </div>
  </template>

<style scoped>
    button {
        color: whitesmoke;
        border: 1px solid white;
    }
    
</style>
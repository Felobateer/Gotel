<script setup>
import * as bootstrap from 'bootstrap'

</script>

<template>
    <div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="../../assets/plan-6c53a4b6.jpg" class="d-block w-100" alt="...">
      <div class="shade">
        <h1 class="text-white fs-1 bg-transparent">Gotel</h1>
        <p class="text-white fs-3">Book your hotel in one minute</p>
        <button class="btn btn-warning">
            <span class="text-white fs-5">Book</span>
        </button>
      </div>
    </div>
    <div class="carousel-item">
      <img src="../../assets/enjoy-b782185f.jpg" class="d-block w-100" alt="...">
      <div class="shade">
        <p class="text-white fs-3">choose your destination</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="../../assets/comfort-b681e3ce.jpg" class="d-block w-100" alt="...">
      <div class="shade">
        <p class="text-white fs-3">Enjoy your trip with us</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
</template>

<style scoped>
    @import '../../style.css';

    #carouselExample {
        margin-bottom: 20px;
        border-radius: 0 0 3rem 3rem;
        overflow: hidden;
    }

    .carousel-item {
        position: relative;
    }

    .carousel-item img {
        width: 100%;
        height: 680px;
        border-radius: 0 0 3rem 3rem;
    }

    .shade {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>
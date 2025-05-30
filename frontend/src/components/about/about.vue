<script>
</script>

<template>
     <article>
      <div id="about" class="text-start">
        <h1 class="text-black text-center mb-5 font-bold bg-transparent">About Us</h1>
        <p class="bg-transparent fs-6 text-black">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias
          facilis excepturi dolorum illo? Tempora maiores suscipit dignissimos
          veniam nulla beatae ipsa ex porro sapiente deserunt, hic, iusto, esse
          nemo sint?Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Maiores, at modi. Atque rerum porro sint obcaecati, dignissimos
          nesciunt! Pariatur laborum magni architecto molestias unde minima.
          Necessitatibus porro velit iste id. Lorem ipsum dolor sit amet
          consectetur adipisicing elit.
        </p>
        <p class="bg-transparent fs-6 text-black">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Veritatis,
          quod sequi mollitia accusantium numquam eos similique ea voluptates
          magnam. Quis omnis eligendi voluptatem beatae totam molestias illum
          fuga eaque aperiam.
        </p>
      </div>
      <div id="aboutImg">
        <img src='/tourist.jpg' alt="tourist" />
      </div>
    </article>
</template>

<style scoped>
article {
  margin: 10rem 0;
  padding: 0 2rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

#about {
  background-color: var(--gold);
  padding: 3rem;
  padding-right: 50%;
  font-size: 1.3rem;
  border-radius: 3rem;
  width: 150%;
  z-index: 100;
}

#aboutImg {
  position: relative;
}

#aboutImg img {
  position: absolute;
  left: 0;
  top: 3rem;
  z-index: 150;
  width: fit-content;
  height: 20rem;
  border-radius: 1rem;
}

@media (max-width: 1000px) {
  article {
    padding: 0 1rem;
    display: block;
  }

  #about {
    padding: 1rem;
    width: 100%;
  }

  #aboutImg {
    display: none;
  }
}
</style>
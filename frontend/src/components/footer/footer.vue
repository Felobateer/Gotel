<script>
</script>

<template>
<footer>
      <div id="footerCol">
        <h1 class="font-bold">Contact</h1>
        <p>Gotel</p>
        <p>
          Pankstr. 33 <span>13357 Berlin</span>
        </p>
      </div>
      <div id="footerCol">
        <p>Tel 123-456-7890</p>
        <p>Email info@Gotel.com</p>
        <p>Book a Consulation</p>
        <div className="d-flex flex-row justify-evenly" id="socialMedia">
            <i class="fa-brands fa-facebook bg-transparent"></i>
            <i class="fa-brands fa-instagram bg-transparent"></i>
            <i class="fa-brands fa-youtube bg-transparent"></i>
        </div>
      </div>
      <div id="footerCol">
        <p>Subscribe to our Newsletter</p>
        <div id="footerForm">
          <input type="text" id="input" className="form" />
          <button className="btn bg-secondary mx-1">Join</button>
        </div>
      </div>
    </footer>
</template>

<style scoped>
  footer {
  position: relative;
  background-color: var(--gold);
  height: 20rem;
  width: 100%;
  align-self: center;
  margin-top: 5rem;
  padding: 5rem 10%;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

#footerCol {
  background: transparent;
  display: flex;
  flex-direction: column;
  justify-content: center;
  place-items: center;
}

#footerCol p,
h1,
span,
div {
  background: transparent;
  color: rgb(20, 20, 20);
}

#footerCol input {
  background-color: white;
  border: none;
  height: 2.4rem;
  border-radius: 0.5rem;
}

#socialMedia {
  margin: 0 auto;
  width: 80%;
  justify-content: space-evenly;
}

@media (max-width: 500px) {
  footer {
    height: 12rem;
    grid-template-columns: repeat(2, 1fr);
    padding: 2rem 10%;
  }

  #footerCol h1 {
    font-size: 1.7rem;
  }

  #footerCol p {
    font-size: 0.9rem;
  }

  #footerCol:last-of-type {
    display: none;
  }
}
</style>
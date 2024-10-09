import "bootstrap/dist/css/bootstrap.min.css";
import tourist from "../assets/tourist.jpg";
import "../styles/homeb.css";

function HomePageb() {
  return (
    <article>
      <div id="about" className="text-start">
        <h1 className=" text-center mb-5 font-bold bg-transparent">About Us</h1>
        <p className="bg-transparent fs-6 ">
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias
          facilis excepturi dolorum illo? Tempora maiores suscipit dignissimos
          veniam nulla beatae ipsa ex porro sapiente deserunt, hic, iusto, esse
          nemo sint?Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Maiores, at modi. Atque rerum porro sint obcaecati, dignissimos
          nesciunt! Pariatur laborum magni architecto molestias unde minima.
          Necessitatibus porro velit iste id. Lorem ipsum dolor sit amet
          consectetur adipisicing elit.
        </p>
        <p className="bg-transparent fs-6 ">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Veritatis,
          quod sequi mollitia accusantium numquam eos similique ea voluptates
          magnam. Quis omnis eligendi voluptatem beatae totam molestias illum
          fuga eaque aperiam.
        </p>
      </div>
      <div id="aboutImg">
        <img src={tourist} alt="tourist" />
      </div>
    </article>
  );
}

export default HomePageb;

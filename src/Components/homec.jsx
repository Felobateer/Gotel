import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/homec.css";
import { Link } from "react-router-dom";
import Berlin from "../assets/Berlin.jpg";
import Munich from "../assets/Munich.jpg";
import Hamburg from "../assets/Hamburg.jpg";
import Darmstadt from "../assets/Darmstadt.jpg";

function HomePagec() {
  const populars = [
    {
      id: 0,
      city: "Berlin",
      hotels: 7,
      average: 154,
      img: Berlin,
    },
    {
      id: 1,
      city: "Munich",
      hotels: 11,
      average: 168,
      img: Munich,
    },
    {
      id: 2,
      city: "Hamburg",
      hotels: 8,
      average: 146,
      img: Hamburg,
    },
    {
      id: 3,
      city: "Darmstadt",
      hotels: 14,
      average: 149,
      img: Darmstadt,
    },
  ];
  return (
    <section>
      <h1 className="text-white fs-1 my-5 text-center">Popular searches</h1>
      <div id="cityCards">
        {populars.map((popular) => (
          <div id="cityCard" key={popular.id}>
            <img src={popular.img} id="cityImg" />
            <p className="text-white text-start py-0 px-3 lh-1">
              {popular.city}
            </p>
            <p className="text-white text-start py-0 px-3 lh-1">
              {popular.hotels} Hotels
            </p>
            <p className="text-white text-start py-0 px-3 lh-1">
              On average &euro; {popular.average}
            </p>
            <Link id="button" className="btn btn-warning" to="/Book">
              Book
            </Link>
          </div>
        ))}
      </div>
    </section>
  );
}

export default HomePagec;

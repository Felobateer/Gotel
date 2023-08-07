import Hotels from "../assets/hotels.json";
import { FaStar } from "react-icons/fa";
import "../styles/results.css";
import Confirmation from "./confirm";

function Results({ primary, secondary }) {
  let filteredHotels = Hotels;

  const filters = (city, price, rating) => {
    if (city) {
      filteredHotels = filteredHotels.filter((hotel) => hotel.city === city);
    }

    switch (price) {
      case 1:
        filteredHotels = filteredHotels.filter((hotel) => hotel.price < 50);
        break;
      case 2:
        filteredHotels = filteredHotels.filter(
          (hotel) => hotel.price > 50 && hotel.price < 100
        );
        break;
      case 3:
        filteredHotels = filteredHotels.filter((hotel) => hotel.price > 100);
        break;
      default:
        break;
    }

    if (rating > 0) {
      filteredHotels = filteredHotels.filter(
        (hotel) => hotel.rating === rating
      );
    }

    return filteredHotels;
  };

  const results = filters(primary.city, secondary.price, secondary.rating);

  if (results.length === 0) {
    return (
      <div id="empty">
        <h1 className="text-white fs-3 p-5">
          We don't have a hotel that fits your selection yet. Please try
          different selections.
        </h1>
      </div>
    );
  } else {
    return (
      <section>
        <h1 className="text-white my-5">Hotels</h1>
        <div id="hotelsGrid">
          {results.map((hotel) => (
            <div id="results" key={hotel.id}>
              <img src={hotel.img} alt={hotel.name} />
              <div className="px-1">
                <div style={{ height: "3rem" }}>
                  <p className="text-white text-start">{hotel.name}</p>
                </div>
                <div
                  className="d-flex flex-row py-2"
                  style={{ justifyContent: "space-between" }}
                  id="resultsRating"
                >
                  <div>
                    <p className="text-white">
                      {hotel.city.charAt(0).toUpperCase() + hotel.city.slice(1)}
                    </p>
                  </div>
                  <div className="d-flex flex-row">
                    {Array.from({ length: hotel.rating }).map((_, index) => (
                      <FaStar key={index} className="text-white" />
                    ))}
                  </div>
                </div>
                <div
                  className="d-flex flex-row py-2"
                  style={{ justifyContent: "space-between" }}
                >
                  <p className="text-white">&euro; {hotel.price}</p>

                  <Confirmation details={hotel} cost={primary} />
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>
    );
  }
}

export default Results;

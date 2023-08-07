import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
import "../styles/homea.css";
import { Link } from "react-router-dom";

function HomePagea() {
  return (
    <main>
      <div
        id="carouselExampleInterval"
        className="carousel slide"
        data-bs-ride="carousel"
      >
        <div className="carousel-inner">
          <div
            id="slide"
            className="carousel-item active"
            data-bs-interval="10000"
          >
            <div id="shade">
              <div id="introText">
                <h1 className="text-white fs-1 bg-transparent">Gotel</h1>
                <p className="text-white fs-3 bg-transparent">
                  Book your hotel in one minute
                </p>

                <Link className="btn btn-warning" to="/Book">
                  Book
                </Link>
              </div>
            </div>
          </div>
          <div id="slide" className="carousel-item" data-bs-interval="2000">
            <div id="shade">
              <div id="introText">
                <p className="text-white fs-3 bg-transparent">
                  choose your destination
                </p>
              </div>
            </div>
          </div>
          <div id="slide" className="carousel-item">
            <div id="shade">
              <div id="introText">
                <p className="text-white fs-3 bg-transparent">
                  Enjoy your{" "}
                  <span id="gold" className=" bg-transparent">
                    trip
                  </span>{" "}
                  with us
                </p>
              </div>
            </div>
          </div>
        </div>
        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleInterval"
          data-bs-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleInterval"
          data-bs-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    </main>
  );
}

export default HomePagea;

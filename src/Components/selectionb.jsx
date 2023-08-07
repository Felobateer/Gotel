import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/selectionb.css";
import { FaStar } from "react-icons/fa";
import { useEffect, useState } from "react";

function SecondarySelection({ setSecondary }) {
  const [rating, setRating] = useState(0);
  const [price, setPrice] = useState(0);
  const [hover, setHover] = useState(null);

  useEffect(() => {
    const secondaryData = {
      price: price,
      rating: rating,
    };
    setSecondary(secondaryData);
  }, [price, rating]);

  const handleCheckboxChange = (event, setterFunction, value) => {
    if (event.target.checked) {
      setterFunction(value);
    }
    console.log(price, rating);
  };

  return (
    <form id="secondarySelection">
      <div id="priceRange">
        <p className="text-white fs-5">Select your price range</p>
        <input
          checked={price === 1}
          onChange={(event) => handleCheckboxChange(event, setPrice, 1)}
          type="checkbox"
          name="price"
          placeholder="0-50"
          id="p1"
          className="d-none"
        />{" "}
        <label htmlFor="p1" className="text-white" id="lowPrice">
          0 to 50&euro;
        </label>
        <input
          checked={price === 2}
          onChange={(event) => handleCheckboxChange(event, setPrice, 2)}
          type="checkbox"
          name="price"
          placeholder="50-100"
          id="p2"
          className="d-none"
        />
        <label htmlFor="p2" className="text-white" id="medPrice">
          50 to 100&euro;
        </label>
        <input
          checked={price === 3}
          onChange={(event) => handleCheckboxChange(event, setPrice, 3)}
          type="checkbox"
          name="price"
          placeholder="100+"
          id="p3"
          className="d-none"
        />
        <label htmlFor="p3" className="text-white" id="highPrice">
          100&euro; +
        </label>
      </div>
      <div id="rating">
        <p className="text-white fs-5">Rating</p>
        <div id="stars">
          {[...Array(5)].map((star, index) => {
            const rate = index + 1;
            return (
              <label>
                <input
                  type="radio"
                  name="rating"
                  value={rate}
                  onClick={() => setRating(rate)}
                />
                <FaStar
                  className="star"
                  color={rate <= (hover || rating) ? "var(--gold)" : "white"}
                  onMouseEnter={() => setHover(rate)}
                  onMouseLeave={() => setHover(rating)}
                />
              </label>
            );
          })}
        </div>
      </div>
    </form>
  );
}

export default SecondarySelection;

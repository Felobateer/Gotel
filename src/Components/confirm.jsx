import { useState, useEffect } from "react";
import { FaStar } from "react-icons/fa";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

const Confirmation = ({ details, cost }) => {
  const [show, setShow] = useState(false);
  const [nights, setNights] = useState(1); // Initialize nights with 0

  useEffect(() => {
    const interval = setInterval(() => {
      const newNights = Math.floor(
        (cost.stay[1] - cost.stay[0]) / (24 * 60 * 60 * 1000)
      );
      setNights(newNights);
    }, 1000);

    return () => {
      clearInterval(interval); // Cleanup the interval when the component unmounts
    };
  }, [cost.stay]); // Run the effect whenever cost.stay changes

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const total = nights * cost.room * details.price;

  return (
    <>
      <button
        className="btn btn-warning"
        type="button"
        data-bs-toggle="modal"
        data-bs-target="confirmation"
        onClick={handleShow}
      >
        Book
      </button>

      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
        className="bg-gray-800"
      >
        <Modal.Header closeButton>
          <Modal.Title>{details.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="d-flex flex-row">
            <div>
              <img src={details.img} alt={details.name} />
            </div>
            <div className="p-5">
              <p className="bg-transparent">&euro; {details.price} per night</p>
              <p className="bg-transparent">{details.city}</p>
              <div className="bg-transparent">
                {Array.from({ length: details.rating }).map((_, index) => (
                  <FaStar
                    key={index}
                    style={{
                      background: "transparent",
                      fill: "var(--background)",
                    }}
                  />
                ))}
              </div>
            </div>
          </div>

          <div>
            <table className="bg-transparent mt-3" style={{ width: "30rem" }}>
              <thead
                className="bg-transparent border-bottom border-blue-800"
                style={{ height: "3rem" }}
              >
                <tr className="bg-transparent">
                  <td className="bg-transparent">Factors</td>
                  <td className="bg-transparent">Cost</td>
                </tr>
              </thead>
              <tbody className="bg-transparent">
                <tr className="bg-transparent">
                  <td className="bg-transparent">price for 1 room per night</td>
                  <td className="bg-transparent">&euro;{details.price}</td>
                </tr>
                <tr className="bg-transparent">
                  <td className="bg-transparent">Rooms</td>
                  <td className="bg-transparent">x {cost.room}</td>
                </tr>
                <tr className="bg-transparent">
                  <td className="bg-transparent">Nights</td>
                  <td className="bg-transparent">x {nights}</td>
                </tr>
                <tr className="bg-transparent">
                  <td className="bg-transparent">Total</td>
                  <td className="bg-transparent">&euro; {total}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cancel
          </Button>
          <Button variant="primary" onClick={() => console.log(cost)}>
            confirm Booking
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default Confirmation;

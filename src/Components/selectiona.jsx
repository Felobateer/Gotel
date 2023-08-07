import { useState, useEffect } from "react";
import { DateRange } from "react-date-range";
import Select from "react-select";
import "react-date-range/dist/styles.css";
import "react-date-range/dist/theme/default.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/selectiona.css";

function MainSelection({ setPrimary }) {
  const today = new Date();
  const tomorrow = new Date(today);
  tomorrow.setDate(tomorrow.getDate() + 1);
  const [openDate, setOpenDate] = useState(false);
  const [stay, setStay] = useState([
    {
      startDate: today,
      endDate: tomorrow,
      key: "selection",
    },
  ]);
  const [adult, setAdult] = useState(1);
  const [child, setChild] = useState(0);
  const [room, setRoom] = useState(1);
  const [city, setCity] = useState("");
  const [showDropdown, setShowDropdown] = useState(false);

  const options = [
    { value: "", label: "Choose your destination" },
    { value: "berlin", label: "Berlin" },
    { value: "munich", label: "Munich" },
    { value: "hamburg", label: "Hamburg" },
    { value: "darmstadt", label: "Darmstadt" },
  ];

  useEffect(() => {
    const startDate = stay[0].startDate;
    const endDate = stay[0].endDate;
    const mainData = {
      city: city,
      stay: [startDate, endDate],
      adult,
      child,
      room,
    };
    setPrimary(mainData);
  }, [city, stay, adult, child, room]);

  const handleToggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  const toggleDatePicker = () => {
    setOpenDate(!openDate);
  };

  const handleCity = (select) => {
    setCity(select.value);
  };

  const formatDate = (date) => {
    return new Date(date).toLocaleDateString("en-US", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    });
  };

  const handleDate = (item) => {
    setStay([
      {
        startDate: item.selection.startDate,
        endDate: item.selection.endDate,
        key: "selection",
      },
    ]);
  };

  const increment = (item) => {
    switch (item) {
      case "adult":
        setAdult(adult + 1);
        break;
      case "child":
        setChild(child + 1);
        break;
      case "room":
        setRoom(room + 1);
        break;
      default:
        return;
    }
  };

  const decrement = (item) => {
    switch (item) {
      case "adult":
        setAdult(adult - 1);
        break;
      case "child":
        setChild(child - 1);
        break;
      case "room":
        setRoom(room - 1);
        break;
      default:
        return;
    }
  };

  return (
    <form>
      <div>
        <Select
          value={city}
          onChange={handleCity}
          options={options}
          placeholder="Choose your destination"
        />
      </div>
      <div id="dates">
        <button
          className="btn btn-primary"
          type="button"
          onClick={toggleDatePicker}
        >
          {stay[0]
            ? formatDate(stay[0].startDate) +
              " to " +
              formatDate(stay[0].endDate)
            : "vacation duration"}
        </button>
        {openDate && (
          <DateRange ranges={stay} onChange={handleDate} minDate={today} />
        )}
      </div>
      <div className="dropdown">
        <button
          className="btn btn-secondary dropdown-toggle"
          type="button"
          onClick={handleToggleDropdown} // Toggle dropdown visibility
          aria-expanded={showDropdown}
        >
          {adult} Adult {child} children {room} room
        </button>
        <ul
          className={`dropdown-menu bg-white ${showDropdown ? "show" : ""}`}
          id="guestCountMenu"
          data-bs-auto-close="false"
        >
          <li>
            <div className="bg-white" id="guestCount">
              <p className="bg-white">Adult</p>
              <div
                className="btn-group"
                role="group"
                aria-label="Basic mixed styles example"
              >
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={() => decrement("adult")}
                >
                  -
                </button>
                <button type="button" className="btn">
                  {adult}
                </button>
                <button
                  type="button"
                  className="btn btn-success"
                  onClick={() => increment("adult")}
                >
                  +
                </button>
              </div>
            </div>
          </li>
          <li>
            <div className="bg-white" id="guestCount">
              <p className="bg-white">Children</p>
              <div
                className="btn-group"
                role="group"
                aria-label="Basic mixed styles example"
              >
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={() => decrement("child")}
                >
                  -
                </button>
                <button type="button" className="btn">
                  {child}
                </button>
                <button
                  type="button"
                  className="btn btn-success"
                  onClick={() => increment("child")}
                >
                  +
                </button>
              </div>
            </div>
          </li>
          <li>
            <div className="bg-white" id="guestCount">
              <p className="bg-white">Room</p>
              <div
                className="btn-group"
                role="group"
                aria-label="Basic mixed styles example"
              >
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={() => decrement("room")}
                >
                  -
                </button>
                <button type="button" className="btn">
                  {room}
                </button>
                <button
                  type="button"
                  className="btn btn-success"
                  onClick={() => increment("room")}
                >
                  +
                </button>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </form>
  );
}

export default MainSelection;

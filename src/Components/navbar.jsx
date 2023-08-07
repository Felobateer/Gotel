import { FaBars } from "react-icons/fa";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
import logo from "../assets/Gotel-logo.jpg";
import "../styles/navbar.css";
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <div id="navbar" className="d-flex flex-row justify-between">
        <div id="GotelLogo">
          <img src={logo} alt="Gotel" />
        </div>
        <div id="gotelNavMenuBtn">
          <button
            className="btn"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#offcanvasRight"
            aria-controls="offcanvasRight"
          >
            <FaBars />
          </button>
        </div>
      </div>
      <div
        className="offcanvas offcanvas-end"
        id="offcanvasRight"
        aria-labelledby="offcanvasRightLabel"
      >
        <div className="offcanvas-header" id="GotelLogo">
          <img src={logo} alt="Gotel" className="mx-auto" />
        </div>
        <div className="offcanvas-body" id="navMenu">
          <ul className="text-white">
            <li data-bs-toggle="offcanvas">
              <Link className="text-white text-decoration-none" to="/">
                Home
              </Link>
            </li>
            <li data-bs-toggle="offcanvas">
              <Link className="text-white text-decoration-none" to="/book">
                Booking
              </Link>
            </li>
            <li data-bs-toggle="offcanvas">
              <Link className="text-white text-decoration-none" to="/join">
                Join Us
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/footer.css";
import { FaFacebookF, FaInstagram, FaYoutube } from "react-icons/fa";

function Footer() {
  return (
    <footer>
      <div id="footerCol">
        <h1 className="font-bold">Contact</h1>
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
          <FaFacebookF className="bg-transparent" />
          <FaInstagram className="bg-transparent" />
          <FaYoutube className="bg-transparent" />
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
  );
}

export default Footer;

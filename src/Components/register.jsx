import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/register.css";
import { useState } from "react";

function Register() {
  const [username, setUsername] = useState("username");

  const handleSignIn = () => {
    const input = document.getElementById("floatingInput").value;
    const password = document.getElementById("floatingPassword").value;
    setUsername(input);
    if (password === "I-like-gotel") {
      alert(`Sign in is successful. Welcome ${input} to Gotel`);
    } else {
      alert("Invalid password. Please try again");
    }
  };

  return (
    <main className="form-signin w-100 m-auto">
      <form id="registerForm">
        <h1 className="h3 mb-3 text-white fw-normal">Please sign in</h1>

        <div className="form-floating">
          <input
            type="text"
            className="form-control"
            id="floatingInput"
            placeholder="name@example.com"
          />
          <label htmlFor="floatingInput" id="usernameLabel">
            Username
          </label>
        </div>
        <div className="form-floating">
          <input
            type="password"
            className="form-control"
            id="floatingPassword"
            placeholder="Password"
          />
          <label htmlFor="floatingPassword" id="passwordLabel">
            Password
          </label>
        </div>

        <div className="form-check text-start my-3">
          <input
            className="form-check-input"
            type="checkbox"
            value="remember-me"
            id="flexCheckDefault"
          />
          <label
            className="form-check-label text-white"
            htmlFor="flexCheckDefault"
          >
            Remember me
          </label>
        </div>
        <button
          className="btn btn-primary w-100 py-2"
          type="submit"
          onClick={handleSignIn}
        >
          Sign in
        </button>
        <p className="mt-5 mb-3 text-white">
          Please put your username and the password I-like-gotel
        </p>
      </form>
    </main>
  );
}

export default Register;

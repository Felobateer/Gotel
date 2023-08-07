import "./App.css";
import Footer from "./Components/footer";
import Navbar from "./Components/navbar";
import AppRoutes from "./router";

function App() {
  return (
    <>
      <Navbar />
      <AppRoutes />
      <Footer />
    </>
  );
}

export default App;

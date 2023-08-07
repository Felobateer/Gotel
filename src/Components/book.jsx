import { useState } from "react";
import Results from "./results";
import MainSelection from "./selectiona";
import SecondarySelection from "./selectionb";
import "../styles/book.css";

function Book() {
  const [primary, setPrimary] = useState([]);
  const [secondary, setSecondary] = useState([]);

  return (
    <>
      <MainSelection setPrimary={setPrimary} />
      <SecondarySelection setSecondary={setSecondary} />
      <Results primary={primary} secondary={secondary} />
    </>
  );
}

export default Book;

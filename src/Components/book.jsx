import { useState } from "react";
import { FiFilter } from "react-icons/fi";
import Results from "./results";
import MainSelection from "./selectiona";
import SecondarySelection from "./selectionb";
import "../styles/book.css";

function Book() {
  const [primary, setPrimary] = useState([]);
  const [secondary, setSecondary] = useState([]);
  const [moreFilter, setMoreFilter] = useState(false);

  return (
    <>
      <section
        className={
          moreFilter ? "selectionSection moreSpace" : "selectionSection"
        }
      >
        <div className="mainSelectionBar">
          <MainSelection setPrimary={setPrimary} />
          <button
            onClick={() => setMoreFilter(!moreFilter)}
            className="btn btn-primary"
            id="moreFilterbtn"
          >
            <FiFilter style={{ background: "none" }} /> Filter
          </button>
        </div>
        {moreFilter ? (
          <div className={moreFilter ? "secondarySelection" : ""}>
            <SecondarySelection setSecondary={setSecondary} />
          </div>
        ) : (
          ""
        )}
      </section>
      <Results primary={primary} secondary={secondary} />
    </>
  );
}

export default Book;

import React, { useState } from "react";
import Register from "./register";
import HompePagec from "./homec";
import MainSelection from "./selectiona";
import SecondarySelection from "./selectionb";
import Results from "./results";

const Root = () => {
  const [primary, setPrimary] = useState([]);
  const [secondary, setSecondary] = useState([]);
  const [tertiary, setTertiary] = useState([]);
  const [isSignin, setIsSignin] = useState(false);

  return (
    <>
      <Register isSignin={isSignin} setIsSignin={setIsSignin} />
      <HompePagec tertiary={tertiary} setTertiary={setTertiary} />
      <MainSelection test={test} />
      <SecondarySelection secondary={secondary} setSecondary={setSecondary} />
      <Results primary={primary} secondary={secondary} tertiary={tertiary} />
    </>
  );
};

export default Root;

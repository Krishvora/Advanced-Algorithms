import Controller from "./Controller";
import ResultStack from "./ResultStack";
import React, { useState } from "react";

const Console = () => {
  const [results, setResults] = useState([]);
  return (
    <>
      <Controller setResults={setResults} />
      <ResultStack results={results} setResults={setResults} />
    </>
  );
};

export default Console;

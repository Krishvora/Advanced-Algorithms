import React from "react";
import Result from "./Result";

const ResultStack = ({ results, setResults }) => {
  return (
    <>
      {results.map((result) => (
        <Result result={result} key={result.id} setResults={setResults} />
      ))}
    </>
  );
};

export default ResultStack;

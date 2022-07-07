import React from "react";
import Form from "react-bootstrap/Form";

const Algorithms = ({ params, handleChange }) => {
  const convert = (text) => {
    const result = text.replace(/([A-Z])/g, " $1");
    const finalResult = result.charAt(0).toUpperCase() + result.slice(1);
    return finalResult;
  };
  return (
    <>
      <Form.Group>
        <h4>Choose an Algorithm</h4>
        {["medianFinding", "quickSort"].map((algorithm, index) => (
          <Form.Check
            key={index}
            label={convert(algorithm)}
            name="algorithm"
            type="radio"
            id={algorithm}
            value={algorithm}
            onChange={handleChange}
            checked={params.algorithm === algorithm}
          />
        ))}
      </Form.Group>
    </>
  );
};

export default Algorithms;

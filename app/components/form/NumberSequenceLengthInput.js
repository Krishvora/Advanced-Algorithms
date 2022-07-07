import React from "react";
import Form from "react-bootstrap/Form";

const NumberSequenceLengthInput = ({ params, handleChange }) => {
  return (
    <>
      <Form.Group className="mb-3" controlId="numberSequenceLength">
        <h4>Input Sequence Length</h4>
        <Form.Control
          type="number"
          max={params.algorithm === "quickSort" ? "2000" : "5000"}
          placeholder="The number sequence length"
          name="numberSequenceLength"
          value={params.numberSequenceLength}
          onChange={handleChange}
        />
        <Form.Text className="text-muted">
          {params.algorithm === "quickSort"
            ? "Number in range [1, 2000]"
            : "Number in range [1, 5000]"}
        </Form.Text>
      </Form.Group>
    </>
  );
};

export default NumberSequenceLengthInput;

import React from "react";
import Form from "react-bootstrap/Form";

const TargetNumberInput = ({ params, handleChange }) => {
  return (
    <>
      <Form.Group className="mb-3" controlId="targetNumber">
        <h4>Target Number</h4>
        <Form.Control
          type="number"
          min="0"
          max={params.numberSequenceLength - 1 || "0"}
          placeholder={
            (params.algorithm === "quickSort" &&
              "Not applied for the quick sort") ||
            (params.randomized === true && "Restricted to the median") ||
            "The target number"
          }
          value={params.targetNumber}
          name="targetNumber"
          onChange={handleChange}
          disabled={
            params.algorithm === "quickSort" || params.randomized === true
          }
        />
        <Form.Text className="text-muted">
          {params.algorithm === "quickSort" || params.randomized === true
            ? "Target number is locked to the median"
            : `Number in range [0, ${params.numberSequenceLength - 1}]`}
        </Form.Text>
      </Form.Group>
    </>
  );
};

export default TargetNumberInput;

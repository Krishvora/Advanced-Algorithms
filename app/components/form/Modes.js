import React from "react";
import Form from "react-bootstrap/Form";

const Modes = ({ params, handleChange }) => {
  return (
    <>
      <Form.Group>
        <h4>Choose Modes</h4>
        {[3, 5, 7].map((amount, index) => (
          <Form.Check
            key={index}
            label={`Linear-Time Group Amount of ${amount}`}
            name={`linearTimeGroupAmount${amount}`}
            type="checkbox"
            id={`linearTimeGroupAmount${amount}`}
            onChange={handleChange}
            checked={params[`linearTimeGroupAmount${amount}`]}
          />
        ))}
        <Form.Check
          label="Randomized"
          name="randomized"
          type="checkbox"
          id="randomized"
          onChange={handleChange}
          checked={params.randomized}
        />
      </Form.Group>
    </>
  );
};

export default Modes;

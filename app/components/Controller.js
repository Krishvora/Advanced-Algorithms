import React, { useState, useEffect } from "react";
import Stack from "react-bootstrap/Stack";
import Button from "react-bootstrap/Button";
import Accordion from "react-bootstrap/Accordion";
import Alert from "react-bootstrap/Alert";
import lambdaUrls from "./lambda-urls";
import TargetNumberInput from "./form/TargetNumberInput";
import Modes from "./form/Modes";
import NumberSequenceLengthInput from "./form/NumberSequenceLengthInput";
import Algorithms from "./form/Algorithms";

const Controller = ({ setResults }) => {
  const [params, setParams] = useState({
    numberSequenceLength: 0,
    algorithm: "",
    linearTimeGroupAmount3: false,
    linearTimeGroupAmount5: false,
    linearTimeGroupAmount7: false,
    randomized: false,
    targetNumber: 0,
  });
  const [count, setCount] = useState(0);
  const [showError, setShowError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    setParams({
      numberSequenceLength: 50,
      algorithm: "medianFinding",
      linearTimeGroupAmount3: false,
      linearTimeGroupAmount5: false,
      linearTimeGroupAmount7: false,
      randomized: false,
      targetNumber: 25,
    });
  }, []);

  const handleChange = (e) => {
    const name = e.target.name;

    let value = "";
    if (e.target.type === "checkbox") {
      value = e.target.checked;
    } else if (e.target.type === "number") {
      value = parseInt(e.target.value);
      value = value > e.target.max ? parseInt(e.target.max) : value;
      value = value < e.target.min ? parseInt(e.target.min) : value;
    } else {
      value = e.target.value;
    }
    if (
      (params.algorithm === "medianFinding" ||
        (name === "algorithm" && value === "medianFinding")) &&
      (params.numberSequenceLength > 0 ||
        (name === "numberSequenceLength" && value > 0)) &&
      (params.randomized || (name === "randomized" && value))
    ) {
      const targetNumber =
        name === "numberSequenceLength"
          ? Math.floor(value / 2)
          : Math.floor(params.numberSequenceLength / 2);
      setParams({
        ...params,
        targetNumber,
        [name]: value,
      });
    } else {
      setParams({ ...params, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (
      [
        params.numberSequenceLength,
        params.linearTimeGroupAmount3 ||
          params.linearTimeGroupAmount5 ||
          params.linearTimeGroupAmount7 ||
          params.randomized,
        (params.algorithm === "medianFinding" && params.randomized) ||
          (params.algorithm === "medianFinding" && params.targetNumber >= 0) ||
          params.algorithm === "quickSort",
      ].every((v) => Boolean(v) === true)
    ) {
      const response = await fetch(lambdaUrls[params.algorithm], {
        method: "POST",
        body: JSON.stringify(params),
      });
      const { body } = await response.json();
      const result = JSON.parse(body);
      result.id = count;
      setCount(count + 1);
      setResults((prev) => [result, ...prev]);
      setShowError(false);
    } else {
      setErrorMessage("Some parameters are not provided");
      setShowError(true);
    }
  };
  return (
    <>
      <Accordion defaultActiveKey="0">
        <Accordion.Item eventKey="0">
          <Accordion.Header>Parameters</Accordion.Header>
          <Accordion.Body>
            <Stack gap={3}>
              <Algorithms params={params} handleChange={handleChange} />
              <Modes params={params} handleChange={handleChange} />
              <NumberSequenceLengthInput
                params={params}
                handleChange={handleChange}
              />
              <TargetNumberInput params={params} handleChange={handleChange} />
              <Button onClick={handleSubmit}>Submit</Button>
            </Stack>
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
      {showError && (
        <Alert
          className="my-2"
          variant="danger"
          onClose={() => {
            setShowError(false);
            setErrorMessage("");
          }}
          dismissible
        >
          <Alert.Heading>{errorMessage || "Unknown Error"}</Alert.Heading>
        </Alert>
      )}
    </>
  );
};

export default Controller;

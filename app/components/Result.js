import React, { useState } from "react";
import Table from "react-bootstrap/Table";
import Accordion from "react-bootstrap/Accordion";

const Result = ({ result }) => {
  const convert = (text) => {
    const result = text.replace(/([A-Z0-9])/g, " $1");
    const finalResult = result.charAt(0).toUpperCase() + result.slice(1);
    return finalResult;
  };
  const {
    report,
    params: { algorithm },
  } = result;
  let { target_number: targetNumber, seq, results } = report;

  const [toggleSeq, setToggleSeq] = useState(false);

  const seqText = [
    seq.replaceAll(",", ", "),
    `${seq.split(",").slice(0, 5).join(", ")} ...`,
  ];

  return (
    <>
      <Accordion className="my-2" defaultActiveKey="0">
        <Accordion.Item eventKey="0">
          <Accordion.Header>
            <b>
              #{result.id} {convert(algorithm)}
            </b>
          </Accordion.Header>
          <Accordion.Body>
            <section>
              <p
                onClick={() => {
                  setToggleSeq(!toggleSeq);
                }}
              >
                <b>Sequence({seq.split(",").length}) </b>
                {toggleSeq ? seqText[0] : seqText[1]}
              </p>
              {algorithm === "medianFinding" && (
                <p>
                  <b>Target Number</b> {targetNumber}
                </p>
              )}
            </section>
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>Mode</th>
                  <th>Time</th>
                  {algorithm === "medianFinding" && <th>Found</th>}
                </tr>
              </thead>
              <tbody>
                {Object.entries(results).map(([key, value], i) => {
                  return (
                    <tr key={i}>
                      <td>{convert(key)}</td>
                      <td>{value.time}</td>
                      {algorithm === "medianFinding" && (
                        <td>{value.found_number}</td>
                      )}
                    </tr>
                  );
                })}
              </tbody>
            </Table>
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    </>
  );
};

export default Result;

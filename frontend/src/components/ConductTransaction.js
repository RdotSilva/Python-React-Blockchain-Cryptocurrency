import React, { useState } from "react";
import { FormGroup, FormControl, Button } from "react-bootstrap";
import { API_BASE_URL } from "../config";

function ConductTransaction() {
  const [amount, setAmount] = useState(0);
  const [recipient, setRecipient] = useState("");

  const updateRecipient = (event) => {
    setRecipient(event.target.value);
  };

  return (
    <div className="ConductTransaction">
      <h3>Conduct a Transaction</h3>
      <br />
      <FormGroup>
        <FormControl
          input="text"
          placeholder="recipient"
          value={recipient}
          onChange={updateRecipient}
        />
      </FormGroup>
    </div>
  );
}

export default ConductTransaction;

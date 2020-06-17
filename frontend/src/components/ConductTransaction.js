import React, { useState } from "react";
import { FormGroup, FormControl, Button } from "react-bootstrap";
import { API_BASE_URL } from "../config";

function ConductTransaction() {
  const [amount, setAmount] = useState(0);
  const [recipient, setRecipient] = useState("");
}

export default ConductTransaction;

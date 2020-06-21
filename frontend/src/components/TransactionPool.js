import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Transaction from "./Transaction";
import { API_BASE_URL } from "../config";

function TransactionPool() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}/transactions`)
      .then((response) => response.json())
      .then((json) => setTransactions(json));
  }, []);
}

export default TransactionPool;

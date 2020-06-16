import React, { useState, useEffect } from "react";
import { API_BASE_URL } from "../config";
import Block from "./Block";

const PAGE_RANGE = 3;

function Blockchain() {
  const [blockchain, setBlockchain] = useState([]);
  const [blockchainLength, setBlockchainLength] = useState(0);

  useEffect(() => {
    fetch(`${API_BASE_URL}/blockchain`)
      .then((response) => response.json())
      .then((json) => setBlockchain(json));
  }, []);

  return (
    <div className="Blockchain">
      <h3>Blockchain</h3>
      <div>
        {blockchain.map((block) => (
          <Block key={block.hash} block={block} />
        ))}
      </div>
    </div>
  );
}

export default Blockchain;

import React, { useState, useEffect } from "react";
import { API_BASE_URL } from "../config";

function Blockchain() {
  const [blockchain, setBlockchain] = useState({});

  return (
    <div className="Blockchain">
      <h3>Blockchain</h3>
      <div>
        {blockchain.map((block) => (
          <div key={block.hash}>{JSON.stringify(block)}</div>
        ))}
      </div>
    </div>
  );
}

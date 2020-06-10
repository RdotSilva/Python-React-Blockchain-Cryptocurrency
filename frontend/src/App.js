import React, { useState, useEffect } from "react";
import logo from "./assets/logo.png";

function App() {
  const [walletInfo, setWalletInfo] = useState({});

  return (
    <div className="App">
      <img className="logo" src={logo} alt="logo" />
      <h3>Welcome to pychain</h3>
    </div>
  );
}

export default App;

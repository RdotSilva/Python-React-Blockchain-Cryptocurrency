import React, { useState } from "react";

function App() {
  const [userQuery, setUserQuery] = useState("");

  const updateUserQuery = (event) => {
    console.log("userQuery:", userQuery);
    setUserQuery(event.target.value);
  };

  return (
    <div className="App">
      <input value={userQuery} onChange={updateUserQuery} />
      <button>Search</button>
    </div>
  );
}

export default App;

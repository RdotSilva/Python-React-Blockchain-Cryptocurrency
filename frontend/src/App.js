import React, { useState } from "react";

function App() {
  const [userQuery, setUserQuery] = useState("");
  return (
    <div className="App">
      <input value={userQuery} onChange={updateUserQuery} />
      <button>Search</button>
    </div>
  );
}

export default App;

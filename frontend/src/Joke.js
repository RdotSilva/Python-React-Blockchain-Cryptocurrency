import React, { useEffect, useState } from "react";

function Joke() {
  const [joke, setJoke] = useState({});

  useEffect(() => {
    fetch("https://official-joke-api.appspot.com/jokes/random")
      .then((response) => response.json())
      .then((json) => console.log("Joke JSON:", json));
    console.log("Fetching data...");
  });

  return (
    <div>
      <h3>Joke</h3>
    </div>
  );
}

export default Joke;

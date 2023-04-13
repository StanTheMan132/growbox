// @format
import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [customers, setCustomers] = useState([]);
  const [error, setError] = useState("");
  const [onTime, setOnTime] = useState<string>("04:00");
  const [offTime, setOffTime] = useState<string>("00:00");

  // Example fetch to get the customer list from the server/db
  useEffect(() => {
    fetch("http://localhost:8000/input/")
      .then((response) => response.json())
      .then((data) => setCustomers(data))
      .catch((error) => setError(error.message));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Wiet Koelkast</h1>
        <div>
          <label>Aan tijd</label>
          <input
            value={onTime}
            onChange={(e) => setOnTime(e.target.value)}
            type="time"
          />
          <label>=Uit tijd</label>
          <input
            value={offTime}
            onChange={(e) => setOffTime(e.target.value)}
            type="time"
          />
        </div>
        {customers.map(({ pk, name }) => (
          <p key={pk}>name: {name}</p>
        ))}
        <p> {error} </p>
      </header>
    </div>
  );
}

export default App;

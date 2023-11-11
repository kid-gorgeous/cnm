import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  // const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
  // const apiPort = process.env.REACT_APP_API_PORT || 5000;

  // TODO: Fetch data from the backend using the Fetch API proxy from package.json if it doesnt worl
  // https://create-react-app.dev/docs/proxying-api-requests-in-development/
  // https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
  // https://developer.mozilla.org/en-US/docs/Web/API/Response
  // https://developer.mozilla.org/en-US/docs/Web/API/Body/json
  // https://developer.mozilla.org/en-US/docs/Web/API/Body/text
  // https://developer.mozilla.org/en-US/docs/Web/API/Body/body



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/api');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result);
      } catch (error) {
        setError(error);
      }
    };

    fetchData();
  }, []); // The empty dependency array means this effect runs once when the component mounts


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <h1>React App</h1>
          {data ? (
            <p>{data.message}</p>
          ) : (
            <p>Fetching data from the server...</p>
          )}
          {error && <p>Error: {error.message}</p>}

          <p>{JSON.stringify(data)}</p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

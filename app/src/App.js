import * as React from 'react';
import Button from '@mui/material/Button';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to our React App. 
        </p>
        
        <Button variant="contained"
          className= "App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer">
          Learn React
        </Button>

        <a
          className = 'Github-link'
          href="https://github.com/Cheat-No-More"
          target="_blank"
          rel="noopener noreferrer"
        >
          Github
        </a>
      </header>
    </div>
  );
}

export default App;

import React from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  useParams,
} from 'react-router-dom';

function App() {
  console.log('here');
  return (
    <div className="App">
      <header className="App-header">
        <p>Edit and save to reload. </p>
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

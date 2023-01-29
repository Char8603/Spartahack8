import logo from './logo.svg';
import './App.css';
import StockForm from './component/input.component.jsx'
import React from 'react';
function App() {

  return (
    <div className="App">
      <header className="App-header">
        <title>Stock</title>
        <div class="main-content">
          <StockForm />
        </div>
      </header>
    </div>
  );
}

export default App;

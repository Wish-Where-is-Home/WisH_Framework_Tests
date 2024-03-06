import React, { useState } from 'react';

import logo from './logo.svg';
import './App.css';

import Navbar from './Section/Navbar/Navbar';
import Home from './Section/Home/Home';

function App() {


  const [darkMode, setDarkMode] = useState(false);


  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    if (darkMode) {
        document.documentElement.classList.remove('dark-mode');
    } else {
        document.documentElement.classList.add('dark-mode');
    }
};

  return (

  
    <div className={`App ${darkMode ? 'dark-mode' : 'light-mode'}`}>
      <Navbar darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>
      <Home/>
    </div>
  );
}

export default App;


import React, { useState } from 'react';
import './App.css';
import Navbar from './Section/Navbar/Navbar';
import Home from './Section/Home/Home';

function App() {
    const [darkMode, setDarkMode] = useState(false);

    const toggleDarkMode = () => {
        setDarkMode(!darkMode);
        document.documentElement.classList.toggle('dark-mode', darkMode);
    };

    return (
        <div className={`App ${darkMode ? 'dark-mode' : 'light-mode'}`}>
            <Navbar darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>
            <Home darkMode={darkMode}/>
        </div>
    );
}

export default App;
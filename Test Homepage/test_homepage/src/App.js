import React, { useState, useEffect } from 'react';
import './App.css';
import Navbar from './Section/Navbar/Navbar';
import Home from './Section/Home/Home';
import Loader from './Section/Loader/Loader';

function App() {
    const [darkMode, setDarkMode] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const prefersDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        setDarkMode(prefersDarkMode);
    }, []);

    const toggleDarkMode = () => {
        setDarkMode(!darkMode);
        document.documentElement.classList.toggle('dark-mode', !darkMode);
    };

    useEffect(() => {
        const timer = setTimeout(() => {
            setLoading(false);
        }, 2000);

        return () => clearTimeout(timer);
    }, []);

    return (
        <div className={`App ${darkMode ? 'dark-mode' : 'light-mode'}`}>
            <Loader visible={loading} /> 
            {!loading && (
                <>
                    <Navbar darkMode={darkMode} toggleDarkMode={toggleDarkMode}/>
                    <Home darkMode={darkMode}/>
                </>
            )}
        </div>
    );
}

export default App;

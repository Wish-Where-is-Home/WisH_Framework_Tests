import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from 'react-router-dom'; 

import './App.css';
import Navbar from './Section/Navbar/Navbar';
import Home from './Section/Home/Home';
import Loader from './Section/Loader/Loader';
import Ndpage from './Page/2ndpage/Ndpage';

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
                    <BrowserRouter>
                        <Routes>
                        <Route exact path="/" element={<Home darkMode={darkMode} />} />
                        <Route path="/ndpage" element={<Ndpage darkMode={darkMode} />} />
                        </Routes>
                    </BrowserRouter>
                </>
            )}
        </div>
    );
}

export default App;

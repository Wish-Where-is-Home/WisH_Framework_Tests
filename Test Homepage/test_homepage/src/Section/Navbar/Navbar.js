import React, { useState } from 'react';
import './Navbar.css';

function Navbar() {
    const [menuOpen, setMenuOpen] = useState(false);
    const [darkMode, setDarkMode] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    const toggleDarkMode = () => {
        setDarkMode(!darkMode);
    };

    return (
      <nav className={`navbar ${darkMode ? 'dark-mode' : 'light-mode'}`}>
            <div className='navbar-container'>
                <div className="logo">
                    <h1>Logo</h1>
                </div>
                <div className="hamburger" onClick={toggleMenu}>
                    <div className={`hamburger-lines ${menuOpen ? 'open' : ''}`}>
                        <span className="line line1"></span>
                        <span className="line line2"></span>
                        <span className="line line3"></span>
                    </div>
                </div>
                <input type="checkbox" className="theme-toggle" onClick={toggleDarkMode} />
            </div>
            {menuOpen && (
                <div className="menu-items">
                    <ul>
                        <li><a href="#">Login</a></li>
                        <li><a href="#">About Us</a></li>
                    </ul>
                </div>
            )}
        </nav>
    );
}

export default Navbar;

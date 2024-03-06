import React, { useState, useEffect } from 'react';
import './Navbar.css';
import logo from './../../logo1.png';

function Navbar({ darkMode, toggleDarkMode }) {
    const [menuOpen, setMenuOpen] = useState(false);
    const [isMobile, setIsMobile] = useState(window.innerWidth < 1000);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    useEffect(() => {
        const handleResize = () => {
            setIsMobile(window.innerWidth < 1000);
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    return (
        <nav className={`navbar ${darkMode ? 'dark-mode' : 'light-mode'}`}>
            <div className='navbar-container'>
                <div className="logo">
                    <img src={logo} alt="logo" />
                </div>
                {isMobile ? (
                    <div className="hamburger" onClick={toggleMenu}>
                        <div className={`hamburger-lines ${menuOpen ? 'open' : ''}`}>
                            <span className="line line1"></span>
                            <span className="line line2"></span>
                            <span className="line line3"></span>
                        </div>
                    </div>
                ) : (
                    <div className="menu-items2">
                        <ul>
                            <li><a href="#">About Us</a></li>
                            <li><a href="#">Login</a></li>
                        </ul>
                    </div>
                )}
                <input type="checkbox" className="theme-toggle" checked={darkMode} onChange={toggleDarkMode} />
            </div>
            {menuOpen && isMobile && (
                <div className="menu-items">
                    <ul>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Login</a></li>
                    </ul>
                </div>
            )}
        </nav>
    );
}

export default Navbar;

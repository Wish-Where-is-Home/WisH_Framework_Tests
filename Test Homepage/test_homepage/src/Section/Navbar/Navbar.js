import React, { useState, useEffect } from 'react';
import './Navbar.css';
import logo from './../../logo1.png';
import {useTranslation} from "react-i18next";
import { LanguageSelector } from '../LanguageSelector/LanguageSelector';

function Navbar({ darkMode, toggleDarkMode }) {

    const {t} = useTranslation("common");


    const [menuOpen, setMenuOpen] = useState(false);
    const [isMobile, setIsMobile] = useState(window.innerWidth < 3000);

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
                            <li><a href="#">{t('aboutus')}</a></li>
                            <li><a href="#">Login</a></li>
                            <li><LanguageSelector style={{"marginleft":"3rem"}}/></li>
                        </ul>
                    </div>
                )}
                <input type="checkbox" className="theme-toggle" checked={darkMode} onChange={toggleDarkMode} />
            </div>
            {menuOpen && isMobile && (
                <div className="menu-items">
                    <ul>
                        <li><a href="#">{t('aboutus')}</a></li>
                        <li><a href="#">Login</a></li>
                        <li><LanguageSelector style={{margin:0}}/></li>
                    </ul>
                </div>
            )}
        </nav>
    );
}

export default Navbar;

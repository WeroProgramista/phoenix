import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';
import Logo from '../assets/pHOENIX_METALOCK.svg';

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar_logo">
                <NavLink exact activeClassName="active" to="/">
                    <img src={Logo} alt='' />
                </NavLink>
            </div>
            <ul className="navbar_menu">
                <li>
                    <NavLink exact activeClassName="active" to="/statki">
                        Statki
                    </NavLink>
                </li>
                <li>
                    <NavLink activeClassName="active" to="/klienci">
                        Klienci
                    </NavLink>
                </li>
                <li>
                    <NavLink activeClassName="active" to="/kalendarz">
                        Kalendarz
                    </NavLink>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;


import {Link} from "react-router-dom";
import {useEffect, useState} from "react";

import isLogged from "../../utils/checkIfLogged";
import authService from "../../services/authService";

import './appHeader.css'

const AppHeader = () => {
    const {logout} = authService();
    const [links, setLinks] = useState((<></>));


    const renderLoggedIn = (
        <>
            <Link className="nav-link" to="/profile">Profile</Link>
            <Link className="nav-link" to="/login" onClick={logout}>Logout</Link>
        </>
    )

    const renderAnonymous = (
        <>
            <Link className="nav-link" to="/login">Sign In</Link>
            <Link className="nav-link" to="/register">Sign Up</Link>
        </>
    )

    useEffect(() => {
        (isLogged() ? setLinks(renderLoggedIn) : setLinks(renderAnonymous))
    }, [links])

    return (
        <header className="header">
            <div className="header-wrapper">
                <div className="shop-title">
                    Online store
                </div>
                <div className="nav-bar">
                    <Link className="nav-link" to="/">Catalog</Link>
                    {links}
                    <Link className="nav-link" to="#">Cart</Link>
                </div>
            </div>
        </header>
    )
}

export default AppHeader;
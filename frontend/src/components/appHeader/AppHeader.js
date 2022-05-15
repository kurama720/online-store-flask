import {Link} from "react-router-dom";
import {useEffect, useState} from "react";

import isLogged from "../../utils/checkIfLogged";
import authService from "../../services/authService";

import './appHeader.css'

const AppHeader = (props) => {
    const {logout} = authService();
    const [logged, setLogged] = useState(false);

    const {totalPrice} = props

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
        isLogged() ? setLogged(true) : setLogged(false)
    }, [])

    return (
        <header className="header">
            <div className="header-wrapper">
                <div className="shop-title">
                    Online store
                </div>
                <div className="nav-bar">
                    <Link className="nav-link" to="/catalog">Catalog</Link>
                    <Link className="nav-link" to='/catalog/upload'>Upload product</Link>
                    {logged ? renderLoggedIn : renderAnonymous}
                    <Link className="nav-link" to="/cart">Cart (${totalPrice.toFixed(2)})</Link>
                </div>
            </div>
        </header>
    )
}

export default AppHeader;
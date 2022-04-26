import React from 'react';
import {Navigate, useLocation} from 'react-router-dom';

import isLogged from "./checkIfLogged";

function RequireAuth({ children }: { children: JSX.Element }) {
    let location = useLocation();

    if (!isLogged()) {
        return <Navigate to="/login" state={{ from: location }} />;
    }
    return children;
}

export default RequireAuth;

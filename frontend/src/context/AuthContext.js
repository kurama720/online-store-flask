import { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import { useNavigate } from "react-router-dom";

const API_URL = process.env.REACT_APP_API_URL;

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
    const [authTokens, setAuthTokens] = useState(() =>
        localStorage.getItem("authTokens")
            ? JSON.parse(localStorage.getItem("authTokens"))
            : null
    );

    const [refreshTokens, setRefreshTokens] = useState(() =>
        localStorage.getItem('refreshTokens'))
            ? JSON.parse(localStorage.getItem("refreshTokens"))
            : null

    const [user, setUser] = useState(() =>
        localStorage.getItem("authTokens")
            ? jwt_decode(localStorage.getItem("authTokens"))
            : null
    );
    const [loading, setLoading] = useState(true);

    const navigate = useNavigate();

    const loginUser = async (email, password) => {
        const response = await fetch(`${API_URL}/auth/login`, {
            method: "POST",
            mode: "cors",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        });
        const data = await response.json();

        if (response.status === 200) {
            setAuthTokens(data.access);
            setRefreshTokens(data.refresh)
            setUser(jwt_decode(data.access));
            localStorage.setItem("authTokens", JSON.stringify(data));
            localStorage.setItem("refreshTokens", JSON.stringify(data));
            navigate.push("/")
        } else {
            alert("Something went wrong!");
        }
    };

    const registerUser = async (email, password) => {
        const response = await fetch(`${API_URL}/auth/register`, {
            method: "POST",
                headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password,
            })
        });
        if (response.status === 201) {
            navigate.push("/login");
        } else {
            alert("Something went wrong!");
        }
    };

    const logoutUser = () => {
        setAuthTokens(null);
        setUser(null);
        localStorage.removeItem("authTokens");
        navigate.push("/");
    };

    const contextData = {
        user,
        setUser,
        authTokens,
        setAuthTokens,
        registerUser,
        loginUser,
        logoutUser
    };

    useEffect(() => {
        if (authTokens) {
            setUser(jwt_decode(authTokens.access));
        }
        setLoading(false);
    }, [authTokens, loading]);

    return (
        <AuthContext.Provider value={contextData}>
            {loading ? null : children}
        </AuthContext.Provider>
    );
}
// import { createContext, useState, useEffect } from "react";
// import jwt_decode from "jwt-decode";
// import { useNavigate } from "react-router-dom";
//
// const API_URL = process.env.REACT_APP_API_URL;
//
// const AuthContext = createContext();
//
// export default AuthContext;
//
// export const AuthProvider = ({ children }) => {
//     const [authTokens, setAuthTokens] = useState(() =>
//         localStorage.getItem("authTokens")
//             ? JSON.parse(localStorage.getItem("authTokens"))
//             : null
//     );
//     const [user, setUser] = useState(() =>
//         localStorage.getItem("authTokens")
//             ? jwt_decode(localStorage.getItem("authTokens"))
//             : null
//     );
//     const [loading, setLoading] = useState(true);
//
//     const history = useNavigate();
//
//     const loginUser = async (email, password) => {
//         const response = await fetch(`${API_URL}/token/`, {
//             method: "POST",
//             mode: "cors",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({
//                 email,
//                 password
//             })
//         });
//         const data = await response.json();
//
//         if (response.status === 200) {
//             setAuthTokens(data);
//             setUser(jwt_decode(data.access));
//             localStorage.setItem("authTokens", JSON.stringify(data));
//             history.push("/protected")
//         } else {
//             alert("Something went wrong!");
//         }
//     };
//
//     const registerUser = async (email, password, password2) => {
//         const response = await fetch(`${API_URL}/register`, {
//         method: "POST",
//             headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//             email,
//             password,
//             password2
//         })
//     });
//     if (response.status === 201) {
//         history.push("/login");
//     } else {
//         alert("Something went wrong!");
//     }
// };
//
// const logoutUser = () => {
//     setAuthTokens(null);
//     setUser(null);
//     localStorage.removeItem("authTokens");
//     history.push("/login");
// };
//
// const contextData = {
//     user,
//     setUser,
//     authTokens,
//     setAuthTokens,
//     registerUser,
//     loginUser,
//     logoutUser
// };
//
// useEffect(() => {
//     if (authTokens) {
//         setUser(jwt_decode(authTokens.access));
//     }
//     setLoading(false);
// }, [authTokens, loading]);
//
// return (
//     <AuthContext.Provider value={contextData}>
//         {loading ? null : children}
//     </AuthContext.Provider>
// );
// }
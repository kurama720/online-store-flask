import axios from "axios";
import {Navigate} from "react-router-dom";

import {refreshHeader} from "./authHeader";
import authService from "./authService";

const RefreshToken = async () => {
    const {getCurrentUser} = authService();
    const token = getCurrentUser();

    if (token && token.refresh) {
        const newTokenResponse = await axios.post(`${process.env.REACT_APP_API_URL}/auth/token`, {},{headers: refreshHeader()})
            .catch(error => {
                if (error.response.msg === 'Token has expired') {
                    return <Navigate to={'/login'} />
                } else {
                    return error
                }
            })
        localStorage.setItem('user', JSON.stringify({'access': newTokenResponse.data.access, 'refresh': token.refresh}));
    } else {
        return {}
    }
}

export default RefreshToken;

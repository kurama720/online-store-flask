import axios from 'axios';

import authHeader from "./authHeader";

// To be modified
const UserService = () => {
    const getPublicContent = () => {
        return axios.get(API_URL + 'all');
    }
    const getUserBoard = () => {
        return axios.get(API_URL + 'user', { headers: authHeader() });
    }
    const getModeratorBoard = () => {
        return axios.get(API_URL + 'mod', { headers: authHeader() });
    }
    const getAdminBoard = () => {
        return axios.get(API_URL + 'admin', { headers: authHeader() });
    }
}
export default UserService;

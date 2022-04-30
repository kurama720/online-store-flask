import axios from "axios";

import authHeader from "./authHeader";
import authService from "./authService";

const useAPIService = () =>  {
    const _apiBase = process.env.REACT_APP_API_URL

    const _s3URL = 'https://onlinestore-media-images.s3.eu-central-1.amazonaws.com/'

    const getAllProducts = async () => {
        return await axios.get(`${_apiBase}/shop/products`)
    }

    const getOneProduct = async (id) => {
        return await axios.get(`${_apiBase}/shop/products/${id}`)
    }

    const getAllCategories = async () => {
        return await axios.get(`${_apiBase}/shop/categories`)
    }

    const loginUser = async (email, password) => {
        return await axios.post(`${_apiBase}/auth/login`, {email, password})
    }

    const registerUser = async (email, password) => {
        return await axios.post(`${_apiBase}/auth/register`, {email, password})
    }

    const getUserInfo = async () => {
        return await axios.get(`${_apiBase}/auth/info`, {headers: authHeader()})
    }

    const uploadProduct = async (data) => {
        const {getCurrentUser} = authService();
        const userToken = getCurrentUser();
        return await axios.post(`${_apiBase}/shop/upload_product`, data, {headers: {
            Authorization: 'Bearer ' + userToken.access
            }})
    }

    return {getAllProducts, getOneProduct, getAllCategories, loginUser, registerUser, getUserInfo, uploadProduct, _s3URL}
}

export default useAPIService;
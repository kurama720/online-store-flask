import axios from "axios";

const useAPIService = () =>  {
    const _apiBase = process.env.REACT_APP_API_URL

    const getAllProducts = async () => {
        return await axios.get(`${_apiBase}/shop/products`)
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

    return {getAllProducts, getAllCategories, loginUser, registerUser}
}

export default useAPIService;
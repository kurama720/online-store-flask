import axios from "axios";

import  {authHeader} from "./authHeader";
import RefreshToken from "./refreshTokenCatch";

const useAPIService = () =>  {
    const _apiBase = process.env.REACT_APP_API_URL

    const _s3URL = 'https://onlinestore-media-images.s3.eu-central-1.amazonaws.com/'

    const getAllProducts = async (param= null) => {
        if (param === null) {
            return await axios.get(`${_apiBase}/shop/products`)
        } else {
            return await axios.get(`${_apiBase}/shop/products?category=${param}`)
        }

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
            .catch(async (error) => {
                const {status} = error.response
                const {msg} = error.response.data
                if (status === 401 && msg === 'Token has expired') {
                    await RefreshToken()
                    return getUserInfo()
                } else {
                    return error
                }
            });
    }

    const uploadProduct = async (data) => {
        return await axios.post(`${_apiBase}/shop/upload_product`, data, {headers: authHeader()})
            .catch(async (error) => {
                const {status} = error.response
                const {msg} = error.response.data
                if (status === 401 && msg === 'Token has expired') {
                    await RefreshToken()
                    return uploadProduct(data)
                } else {
                    return error
                }
            });
    }

    const editProduct = async (data, id) => {
        return await axios.put(`${_apiBase}/shop/update_product/${id}`, data, {headers: authHeader()})
            .catch(async (error) => {
                const {status} = error.response
                const {msg} = error.response.data
                if (status === 401 && msg === 'Token has expired') {
                    await RefreshToken()
                    return editProduct(data, id)
                } else {
                    return error
                }
            })
    }

    const deleteProduct = async (id) => {
        return await axios.delete(`${_apiBase}/shop/delete_product/${id}`, {headers: authHeader()})
            .catch(async (error) => {
                const {status} = error.response
                const {msg} = error.response.data
                if (status === 401 && msg === 'Token has expired') {
                    await RefreshToken()
                    return deleteProduct(id)
                } else {
                    return error
                }
            });
    }

    const createCategory = async (name) => {
        return await axios.post(`${_apiBase}/admin_managing/create_category`, {name})
    }

    return {_apiBase, _s3URL, getAllProducts, getOneProduct, getAllCategories, loginUser, registerUser, getUserInfo, uploadProduct, editProduct, deleteProduct, createCategory}
}

export default useAPIService;

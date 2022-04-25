import axios from "axios";
// import useAxios from "../utils/useAxios";

const useAPIService = () =>  {
    const _apiBase = process.env.REACT_APP_API_URL

    // const api = useAxios()

    const getAllProducts = async () => {
        return await axios.get(`${_apiBase}/shop/products`)
    }

    const getAllCategories = async () => {
        return await axios.get(`${_apiBase}/shop/categories`)
    }

    return {getAllProducts, getAllCategories}
}

export default useAPIService;
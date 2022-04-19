import axios from "axios";

const useAPIService = () =>  {
    const _apiBase = 'http://localhost:8000'

    const getAllProducts = async () => {
        return await axios.get(`${_apiBase}/shop/products`)
    }

    return {getAllProducts}
}

export default useAPIService;
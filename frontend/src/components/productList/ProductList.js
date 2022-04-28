import {useState, useEffect} from "react";

import ProductListItem from "../productListItem/ProductListItem";
import useAPIService from "../../services/APIService";

import './productList.css'

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const {getAllProducts} = useAPIService();

    useEffect (() => {
        getAllProducts().then(response => setProducts(response.data.products))
        //eslint-disable-next-line
    }, [])

    const elements = products.map(item => {
        return (
            <ProductListItem
                key={item.id}
                {...item}
                />
        )
    })

    return (
        <div className='product-list'>
            {elements}
        </div>
    )
}

export default ProductList;
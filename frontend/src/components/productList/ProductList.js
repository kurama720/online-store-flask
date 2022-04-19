import {useState} from "react";
import {useEffect} from "react";
import ProductListItem from "../productListItem/ProductListItem";
import useAPIService from "../../services/APIService";

import './productList.css'

const ProductList = () => {

    const [products, setProducts] = useState([]);
    const {getAllProducts} = useAPIService();

    useEffect (() => {
        getAllProducts().then(obj => setProducts(obj.data.products))
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
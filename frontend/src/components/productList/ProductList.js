import {useState, useEffect} from "react";
import {useLocation} from "react-router-dom";

import ProductListItem from "../productListItem/ProductListItem";
import useAPIService from "../../services/APIService";

import './productList.css'

const ProductList = (props) => {
    const [products, setProducts] = useState([]);
    const {getAllProducts} = useAPIService();

    const {handleCartAdd, handleCartRemove, cartProducts} = props

    const query = new URLSearchParams(useLocation().search)
    const category = query.get('category')

    useEffect (() => {
        getAllProducts(category).then(response => setProducts(response.data.products))
        //eslint-disable-next-line
    }, [category])

    const elements = products.map(item => {
        return (
            <ProductListItem
                key={item.id}
                {...item}
                cartProducts={cartProducts}
                handleCartAdd={handleCartAdd}
                handleCartRemove={handleCartRemove}
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
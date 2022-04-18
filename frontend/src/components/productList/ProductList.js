import {useState} from "react";
import {useEffect} from "react";
import axios from "axios";
import ProductListItem from "../productListItem/ProductListItem";

const ProductList = () => {

    const [product, setProduct] = useState();

    useEffect (() => {
      const apiURL = 'http://localhost:8000/shop/products';
      axios.get(apiURL)
          .then((res) => {
              const allProducts = res.data;
              setProduct(allProducts)
          })
    }, [setProduct])

    // const elements = product.map(item => {
    //     const {...itemProps} = item
    //     return (
    //         <ProductListItem
    //             key={item.id}
    //             {...itemProps} />
    //     )
    // })

    return (
        <div>
        </div>
    )
}

export default ProductList;
import CategoryList from "../../components/categoryList/CategoryList";
import ProductList from "../../components/productList/ProductList";

import './catalogPage.css'

const CatalogPage = (props) => {
    const {handleCartAdd, handleCartRemove, cartProducts} = props

    return (
        <div className='wrapper-shop'>
            <CategoryList />
            <ProductList cartProducts={cartProducts} handleCartAdd={handleCartAdd} handleCartRemove={handleCartRemove} />
        </div>
    );
}

export default CatalogPage;
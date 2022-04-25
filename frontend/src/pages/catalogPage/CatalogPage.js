import CategoryList from "../../components/categoryList/CategoryList";
import ProductList from "../../components/productList/ProductList";

import './catalogPage.css'

const CatalogPage = () => {
    return (
        <div className="catalog">
            <div className='wrapper-shop'>
                <CategoryList />
                <ProductList />
            </div>
        </div>
    );
}

export default CatalogPage;
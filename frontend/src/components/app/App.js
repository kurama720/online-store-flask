import {BrowserRouter, Route, Routes} from "react-router-dom";
import {useState} from "react";

import AppHeader from "../appHeader/AppHeader";
import CatalogPage from "../../pages/catalogPage/CatalogPage";
import LoginMenu from "../signInMenu/LoginMenu";
import SignUpMenu from "../signUpMenu/SignUpMenu";
import RequireAuth from "../../utils/requireAuth";
import UserProfile from "../userProfile/UserProfile";
import ProductDetail from "../productDetail/ProductDetail";
import UploadProduct from "../uploadProduct/UploadProduct";
import EditProduct from "../editProduct/EditProduct";
import DeleteProduct from "../deleteProduct/deleteProduct";
import Cart from "../cart/Cart";
import CreateCategory from "../createCategory/CreateCategory";

import './App.css';

const App = () => {

    const [cartProducts, setCartProducts] = useState([]);
    const [totalPrice, setTotalPrice] = useState(0);

    const handleCartAdd = (productObject) => {
        setTotalPrice(totalPrice + productObject.price);
        cartProducts.push(productObject);
    };

    const handleCartRemove = (productObject) => {
        const index = cartProducts.findIndex(product => product.id === productObject.id);
        if (index >= 0) {
            cartProducts.splice(index, 1);
            if (!(totalPrice <= 0)) {
                setTotalPrice(totalPrice - productObject.price)
            };
        };
    };

    const onClearCart = () => {
        setCartProducts([]);
        setTotalPrice(0);
    };

    return (
        <BrowserRouter>
            <div className="App">
                <AppHeader totalPrice={totalPrice} />
                <Routes>
                    <Route path='/catalog' element={<CatalogPage cartProducts={cartProducts} handleCartAdd={handleCartAdd} handleCartRemove={handleCartRemove} />} />
                    <Route path='/catalog/:productId' element={<ProductDetail />} />
                    <Route path='/login' element={ <LoginMenu />} />
                    <Route path='/register' element={ <SignUpMenu />} />
                    <Route path='/profile' element={<RequireAuth> <UserProfile/> </RequireAuth>} />
                    <Route path='/catalog/upload' element={<RequireAuth> <UploadProduct /> </RequireAuth>} />
                    <Route path='/catalog/edit/:productId' element={<RequireAuth> <EditProduct /> </RequireAuth>} />
                    <Route path='/catalog/delete/:productId' element={<RequireAuth> <DeleteProduct /> </RequireAuth>} />
                    <Route path='/cart' element={<Cart cartProducts={cartProducts} onClearCart={onClearCart} totalPrice={totalPrice} />} />
                    <Route path='/create_category' element={<CreateCategory />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;

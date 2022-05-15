import {Link} from "react-router-dom";

import './cart.css'

const Cart = (props) => {
    const {cartProducts, onClearCart, totalPrice} = props
    // // Count amount of each product
    const amountedCartProduct = cartProducts.map((item) => {
        return ({
            ...item,
            amount: cartProducts.filter((obj) => obj.id === item.id).length
        })
    })
    // Remove duplicates
    const noDuplicateProducts = amountedCartProduct.filter((value, index, arr) => arr.findIndex( value2 => (value2.id === value.id)) === index)
    
    
    const elements = noDuplicateProducts.map((item) => {
        return (
            <Link to={`../catalog/${item.id}`} key={item.id}>
                <div className='cart-item'>
                    <p className='cart-item-property'>Name: {item.name.length > 10 ? item.name.slice(0, 10) + '...' : item.name}</p>
                    <p className='cart-item-property'>Amount: {item.amount}</p>
                    <p className='cart-item-property'>Price: ${(item.amount * item.price).toFixed(2)}</p>
                </div>
            </Link>
        )
    })

    const onBuyCart = () => {
        alert("Congratulations! You've bought all the products in the cart!")
        onClearCart()
    }

    return (
        <div className='cart-wrapper'>
            <div className='cart-title'>Cart</div>
            <div className='cart-list'>
                {elements}
            </div>
            {cartProducts.length
                ? <div className='total-price'>Total price: ${totalPrice.toFixed(2)}</div>
                : <div className='empty-cart-msg'>You have not added any products</div>
            }
            {cartProducts.length
                ? <div className='cart-btn-wrapper'>
                    <button className='cart-btn clear' onClick={onClearCart}>Clear</button>
                    <button className='cart-btn buy' onClick={onBuyCart}>Buy</button>
                  </div>
                : <></>
            }
        </div>
    )
}

export default Cart;
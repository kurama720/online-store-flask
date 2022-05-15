import {useState, useEffect} from 'react'
import {Link} from "react-router-dom";
import moment from "moment";

import img404 from '../../resources/img/404.jpeg'
import useAPIService from "../../services/APIService";

import './productListItem.css'

const ProductListItem = (props) => {
    const {id, name, category, created, price, owner, description, image, handleCartAdd, handleCartRemove, cartProducts} = props;
    const {_s3URL} = useAPIService();

    const [amount, setAmount] = useState(0);

    useEffect(() => {
        setAmount(cartProducts.filter((obj) => obj.id === id)?.length)
    }, [cartProducts, id])

    const onClickAdd = () => {
        setAmount(amount + 1)
        handleCartAdd({id: id, name: name, price: price})
    }

    const onClickRemove = () => {
        if (amount > 0) {
            setAmount(amount - 1)
        }
        handleCartRemove({id: id, price: price})
    }

    return (
        <div className="product-list-item">
            <Link to={`../catalog/${id}`}>
                <div>
                    <img className='product-photo' src={image ? `${_s3URL}${image}` : img404} alt="Product"></img>
                    <div className="product-info">
                        <p className="product-title">Name: {name.length > 30 ? name.slice(0, 25) + '...' : name}</p>
                        <p className="product-desc">Description: {description.length > 20 ? description.slice(0, 20) + '...' : description}</p>
                        <p className="product-price">Price: ${price}</p>
                        <p className="product-price">Uploaded: {moment(created).format("YYYY-MM-DD")}</p>
                        <p className="product-price">Category: {category}</p>
                        <p className="product-price">Owner: {owner}</p>
                    </div>
                </div>
            </Link>
            <div className='btn-cart-wrapper'>
                <button className='btn-cart' onClick={onClickRemove}>-</button>
                <p>{amount}</p>
                <button className='btn-cart' onClick={onClickAdd}>+</button>
            </div>
        </div>
    )
}

export default ProductListItem;

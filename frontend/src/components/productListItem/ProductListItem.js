import {Link} from "react-router-dom";

import img404 from '../../resources/404.jpeg'

import './productListItem.css'

const ProductListItem = (props) => {
    const {id, name, category, created, price, owner, description, image} = props
    console.log(`http://localhost:8000/shop/image${image}`)
    return (
        <div className="product">
            <Link to={`../catalog/${id}`}>
                <div>
                    <img className='product-photo' src={`localhost:8000/shop/image`} alt="Product"></img>
                        <div className="product-info">
                            <p className="product-title">{name}</p>
                            <p className="product-desc">{description}</p>
                            <p className="product-price">{price}</p>
                            <p className="product-price">{created}</p>
                            <p className="product-price">{category}</p>
                            <p className="product-price">{owner}</p>
                        </div>
                </div>
            </Link>
        </div>

    )
}

export default ProductListItem;
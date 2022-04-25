import './productListItem.css'
import img404 from '../../resources/img/404.jpeg'

const ProductListItem = (props) => {
    const {name, category, created, price, owner, description} = props
    return (
        <div className="product">
            <img className='product-photo' src={img404} alt="Product"></img>
                <div className="product-info">
                    <p className="product-title">{name}</p>
                    <p className="product-desc">{description}</p>
                    <p className="product-price">{price}</p>
                    <p className="product-price">{created}</p>
                    <p className="product-price">{category}</p>
                    <p className="product-price">{owner}</p>
                </div>
        </div>
    )
}

export default ProductListItem;
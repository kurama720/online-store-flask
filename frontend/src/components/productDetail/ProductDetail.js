import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import moment from "moment";

import useAPIService from "../../services/APIService";
import img404 from '../../resources/img/404.jpeg'

import './productDetail.css'

const ProductDetail = () => {
    const [product, setProduct] = useState({});
    const {getOneProduct, _s3URL} = useAPIService();
    const {productId} = useParams();

    useEffect(() => {
        getOneProduct(productId).then(response => {
            setProduct(response.data)
        })
        //eslint-disable-next-line
    }, [])

    return (
        <div className='detail-wrapper'>
            <img src={product.image ? _s3URL + product.image : img404} alt='Product illustration' className='detail-photo'></img>
            <div className='detail-item'><span className='detail-property'>Name</span>: {product.name}</div>
            <div className='detail-item'><span className='detail-property'>Description</span>: {product.description}</div>
            <div className='detail-item'><span className='detail-property'>Price</span>: {product.price}$</div>
            <div className='detail-item'><span className='detail-property'>Category</span>: {product.category}</div>
            <div className='detail-item'><span className='detail-property'>Owner</span>: {product.owner}</div>
            <div className='detail-item'><span className='detail-property'>Uploaded</span>: {moment(product.created).format("YYYY-MM-DD")}</div>
        </div>
    )
}

export default ProductDetail;
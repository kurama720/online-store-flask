import {useParams} from "react-router-dom";
import {useNavigate} from "react-router-dom";

import useAPIService from "../../services/APIService";

import './deleteProduct.css'

const DeleteProduct = () => {
    const {deleteProduct} = useAPIService();

    const {productId} = useParams();
    const navigate = useNavigate();

    const onDeleteProduct = () => {
        deleteProduct(productId)
            .then(() => navigate('../profile'))
            .catch()
    }

    const onCancel = () => {
        navigate('../profile')
    }

    return (
        <div className='delete-wrapper'>
            <div className='question'>
                <p>Are you sure you want to delete the product?</p>
            </div>
            <div className='btn-wrapper'>
                <button className='btn btn-confirm' onClick={onDeleteProduct}>Yes</button>
                <button className='btn btn-cancel' onClick={onCancel}>No</button>
            </div>
        </div>
    )
}

export default DeleteProduct;
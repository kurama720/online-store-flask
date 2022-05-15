import {useEffect, useState} from "react";
import {useNavigate, useParams} from "react-router-dom";

import useAPIService from "../../services/APIService";

import './editProduct.css'

const EditProduct = () => {
    const [categoryOption, setCategoryOption] = useState([]);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [errorMessage, setErrorMessage] = useState({});

    const {getAllCategories, getOneProduct, editProduct} = useAPIService();
    const navigate = useNavigate()
    const {productId} = useParams()

    const [name, setName] = useState('');
    const [category, setCategory] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] = useState('');
    const [price, setPrice] = useState('');

    const handleChangeName = (event) => {
        setName(event.target.value)
    }

    const handleChangeCategory = (event) => {
        setCategory(event.target.value)
    }

    const handleChangeDescription = (event) => {
        setDescription(event.target.value)
    }

    const handleChangeImage = async (event) => {
        setImage(event.target.files[0])
    }

    const handleChangePrice = (event) => {
        setPrice(event.target.value)
    }

    useEffect(() => {
        getOneProduct(productId).then(response => {
            const product = response.data
            setName(product.name)
            setDescription(product.description)
            setImage(product.image)
            setPrice(product.price)
            setCategory(product.category)
        })
        getAllCategories().then(response => setCategoryOption(response.data.categories))
        //eslint-disable-next-line
    }, [])

    const categoryElements = categoryOption.map(item => {
        return (
            <option value={item.category} key={item.id}>{item.category}</option>
        )
    })

    const renderErrorMessage = (name) =>
        name === errorMessage.name && (
            <div className='login-error'>{errorMessage.message}</div>
        );

    const onHandleSubmitted = (event) => {
        event.preventDefault();
        if (category.length === 0) {
            setErrorMessage({name: 'category', message: 'Select a category'})
        } else if (isNaN(price) || price.length === 0) {
            setErrorMessage({name: 'price', message: 'Price must be numeric'})
        } else if (name.length === 0) {
            setErrorMessage({name: 'name', message: 'Name is required'})
        } else {
            let formData = new FormData();
            if (image) {
                formData.append('image', image, name)
            }
            formData.append('name', name)
            formData.append('price', price)
            formData.append('category', category)
            formData.append('description', description)
            editProduct(formData, productId)
                .then(() => setIsSubmitted(true))
                .catch(() => setErrorMessage({name: 'submit', message: "Something went wrong"}))
        }
    }

    const renderForm = (
        <form onSubmit={onHandleSubmitted}>
            <div className='upload-input'>
                <label className='upload-label'>Product name</label>
                <input placeholder='Tea' type='text' name='name' value={name} onChange={handleChangeName}/>
                {renderErrorMessage('name')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Category</label>
                <select value={category} name='category' onChange={handleChangeCategory}>
                    <option value={category}>{category}</option>
                    {categoryElements}
                </select>
                {renderErrorMessage('category')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Description</label>
                <input placeholder='Tasty tea' value={description} name='description' onChange={handleChangeDescription}/>
                {renderErrorMessage('description')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Image</label>
                <input type='file' name='image' onChange={handleChangeImage}/>
                {renderErrorMessage('image')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Price</label>
                <input placeholder='2.49' type='number' step='0.01' value={price} name='price' onChange={handleChangePrice}/>
                {renderErrorMessage('price')}
            </div>
            <div className='upload-button'>
                <input type='submit' name='submit' value='Upload'/>
                {renderErrorMessage('submit')}
            </div>
        </form>
    )

    return (
        <div className='upload-form'>
            <div className='upload-title'>Upload product</div>
            {isSubmitted ? navigate(`../profile`) : renderForm}
        </div>
    )
}

export default EditProduct;
import {useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";
import useAPIService from "../../services/APIService";

import './uploadProduct.css'

const UploadProduct = () => {
    const [name, setName] = useState('');
    const [category, setCategory] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] = useState('');
    const [price, setPrice] = useState('');
    const [categoryOption, setCategoryOption] = useState([]);
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [errorMessage, setErrorMessage] = useState({});

    const {getAllCategories, uploadProduct} = useAPIService();
    const navigate = useNavigate()

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
        setPrice(Number(event.target.value))
    }

    useEffect (() => {
        getAllCategories().then(response => setCategoryOption(response.data.categories))
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
            formData.append('image', image, name)
            formData.append('name', name)
            formData.append('price', price)
            formData.append('category', category)
            formData.append('description', description)
            uploadProduct(formData)
                .then(() => setIsSubmitted(true))
                .catch(() => setErrorMessage({name: 'submit', message: "Something went wrong"}))
        }
    }

    const renderForm = (
        <form onSubmit={onHandleSubmitted}>
            <div className='upload-input'>
                <label className='upload-label'>Product name</label>
                <input type='text' name='name' value={name} onChange={handleChangeName}/>
                {renderErrorMessage('name')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Category</label>
                <select value={category} name='category' onChange={handleChangeCategory}>
                    <option>...</option>
                    {categoryElements}
                </select>
                {renderErrorMessage('category')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Description</label>
                <input value={description} name='description' onChange={handleChangeDescription}/>
                {renderErrorMessage('description')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Image</label>
                <input type='file' name='image' onChange={handleChangeImage}/>
                {renderErrorMessage('image')}
            </div>
            <div className='upload-input'>
                <label className='upload-label'>Price</label>
                <input type='number' name='price' onChange={handleChangePrice}/>
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
            {isSubmitted ? navigate('/catalog') : renderForm}
        </div>
    )
}

export default UploadProduct;
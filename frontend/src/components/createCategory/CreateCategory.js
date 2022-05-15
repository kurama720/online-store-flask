import {useState} from "react";
import {useNavigate} from "react-router-dom";

import useAPIService from "../../services/APIService";

import './createCategory.css'

const CreateCategory = () => {
    const [name, setName] = useState('');
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [errorMessage, setErrorMessage] = useState({});

    const {createCategory} = useAPIService();
    const navigate = useNavigate()

    const handleChangeName = (event) => {
        setName(event.target.value)
    }

    const renderErrorMessage = (name) =>
        name === errorMessage.name && (
            <div className='category-error'>{errorMessage.message}</div>
        );

    const onHandleSubmitted = (event) => {
        event.preventDefault();
        if (!(name.length >= 2)) {
            setErrorMessage({name: 'name', message: 'Category name is too short'})
        } else {
            createCategory(name)
                .then(() => setIsSubmitted(true))
                .catch((err) => {
                    setErrorMessage({name: 'submit', message: "Something went wrong"})
                })
        }
    }

    const renderForm = (
        <form onSubmit={onHandleSubmitted}>
            <div className='category-input'>
                <label className='category-label'>Category name</label>
                <input placeholder='Tea' type='text' name='name' value={name} onChange={handleChangeName}/>
                {renderErrorMessage('name')}
            </div>
            <div className='category-button'>
                <input type='submit' name='submit' value='Create'/>
                {renderErrorMessage('submit')}
            </div>
        </form>
    )

    return (
        <div className='category-form'>
            <div className='category-title'>Create category</div>
            {isSubmitted ? navigate('/catalog') : renderForm}
        </div>
    )
}

export default CreateCategory;
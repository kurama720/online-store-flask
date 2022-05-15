import {useState, useEffect} from "react";
import {Link, useNavigate} from "react-router-dom";

import useAPIService from "../../services/APIService";

import imgEdit from '../../resources/img/edit-icon.png';
import imgDelete from '../../resources/img/delete-icon.jpg'
import './userProfile.css';


const UserProfile = () => {
    const {getUserInfo} = useAPIService();
    const [email, setEmail] = useState('');
    const [products, setProducts] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        getUserInfo()
            .then(response => {
                setEmail(response.data.user.email);
                setProducts(response.data.user.products);
            })
            .catch(() => {
                navigate('/login')
            })
        //eslint-disable-next-line
    }, []);

    const elements_names = products.map(item => {
        return (
            <li key={item.id} className='profile-list-item'>
                <Link to={`../catalog/${item.id}`}>{item.name}</Link>
                <div>
                    <Link to={`../catalog/edit/${item.id}`}><img src={imgEdit} className='manage-icon' alt='Edit'></img></Link>
                    <Link to={`../catalog/delete/${item.id}`}><img src={imgDelete} className='manage-icon' alt='Delete'></img></Link>
                </div>
            </li>
        )
    })

    return (
        <div className='user-profile'>
            <div className='profile-email'>Email: <span className='email-text'>{email}</span></div>
            {elements_names.length
                ? <div className='profile-list'>Owned products: <ul>{elements_names}</ul></div>
                : <p>No owned products</p>}
        </div>
    )
}

export default UserProfile;

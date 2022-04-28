import {useState, useEffect} from "react";
import {Link, useNavigate} from "react-router-dom";

import useAPIService from "../../services/APIService";

import './userProfile.css'


const UserProfile = () => {
    const {getUserInfo} = useAPIService();
    const [email, setEmail] = useState('');
    const [products, setProducts] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        getUserInfo().then(response => {
            setEmail(response.data.user.email);
            setProducts(response.data.user.products);
        }).catch(() => {
            navigate('/login')
        })
        //eslint-disable-next-line
    }, []);

    const elements_names = products.map(item => {
        return (
            <li key={item.id} className='profile-list-item'><Link to={`../catalog/${item.id}`}>{item.name}</Link></li>
        )
    })

    return (
        <div className='user-profile'>
            <div className='profile-email'>Email: {email}</div>
            <div className='profile-list'>Owned products: <ul>{elements_names}</ul></div>
        </div>
    )
}

export default UserProfile;
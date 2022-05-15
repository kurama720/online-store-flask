import {Link} from "react-router-dom";
import {useState, useEffect} from "react";

import useAPIService from "../../services/APIService";
import CategoryListItem from "../categoryListItem/CategoryListItem";

import './categoryList.css'

const CategoryList = () => {

    const [categories, setCategories] = useState([]);
    const {getAllCategories} = useAPIService();

    useEffect (() => {
        getAllCategories().then(obj => setCategories(obj.data.categories))
        //eslint-disable-next-line
    }, [])

    const elements = categories.map(item => {
        return (
            <CategoryListItem
                key={item.id}
                category={item.category}
            />
        )
    })

    return (
        <div className='categories-list'>
            <p>Categories:</p>

            <ul>
                <li><Link to='/catalog'>All</Link></li>
                {elements}
            </ul>
            <Link to='/create_category'>Create category</Link>
        </div>
    )
}

export default CategoryList;

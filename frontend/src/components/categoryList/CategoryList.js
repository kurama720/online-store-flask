import {useState, useEffect} from "react";

import useAPIService from "../../services/APIService";
import CategoryListItem from "../categoryListItem/CategoryListItem";

import './categoryList.css'

const CategoryList = () => {

    const [categories, setCategories] = useState([]);
    const {getAllCategories} = useAPIService();

    useEffect (() => {
        getAllCategories().then(obj => setCategories(obj.data.categories))
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
                <li><a href='#'>All</a></li>
                {elements}
            </ul>
        </div>
    )
}

export default CategoryList;

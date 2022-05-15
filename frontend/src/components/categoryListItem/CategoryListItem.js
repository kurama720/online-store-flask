import './category.css'
import {Link} from "react-router-dom";

const CategoryListItem = (props) => {
    let {category} = props

    if (category === null) {
        category = 'Other'
    }
    return (
        <li>
            <div className='category'>
                <Link to={`/catalog?category=${category}`}>{category}</Link>
            </div>
        </li>
    )
}

export default CategoryListItem;

import './category.css'

const CategoryListItem = (props) => {
    let {category} = props

    if (category === null) {
        category = 'Other'
    }
    return (
        <li>
            <div className='category'>
                <a href='#'>{category}</a>
            </div>
        </li>
    )
}

export default CategoryListItem;

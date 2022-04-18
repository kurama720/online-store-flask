const ProductListItem = (props) => {
    const {name, category} = props

    return (
        <div>
            <p>{name}</p>
            <p>{category}</p>
        </div>
    )
}

export default ProductListItem;
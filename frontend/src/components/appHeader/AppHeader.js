import './appHeader.css'

const AppHeader = () => {
    return (
        <header className="header">
            <div className="header-wrapper">
                <div className="shop-title">
                    Online store
                </div>
                <div className="nav-bar">
                    <a className="nav-link" href="/">Catalog</a>
                    <a className="nav-link" href="/login">Sign In</a>
                    <a className="nav-link" href="/register">Sign Up</a>
                    <a className="nav-link" href="#">Cart</a>
                </div>
            </div>
        </header>
    )
}

export default AppHeader;
import AppHeader from "../appHeader/AppHeader";
import ProductList from "../productList/ProductList";
import Category from "../categoryListItem/Category";

import './App.css';

const App = () => {
  return (
    <div className="App">
      <AppHeader />
      <div className='wrapper-shop'>
          <Category />
          <ProductList />
      </div>
    </div>
  );
}

export default App;

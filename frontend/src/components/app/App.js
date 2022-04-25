import AppHeader from "../appHeader/AppHeader";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import CatalogPage from "../../pages/catalogPage/CatalogPage";
import LoginMenu from "../loginMenu/LoginMenu";
import SignUpMenu from "../signUpMenu/SignUpMenu";

import './App.css';

const App = () => {
  return (
  <BrowserRouter>
    <div className="App">
      <AppHeader />
      <Routes>
          <Route path='/' element={ <CatalogPage />} />
          <Route path='/login' element={ <LoginMenu />} />
          <Route path='/register' element={ <SignUpMenu />} />
      </Routes>
    </div>
  </BrowserRouter>
  );
}

export default App;

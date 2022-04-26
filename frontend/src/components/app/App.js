import {BrowserRouter, Route, Routes} from "react-router-dom";

import AppHeader from "../appHeader/AppHeader";
import CatalogPage from "../../pages/catalogPage/CatalogPage";
import LoginMenu from "../signInMenu/LoginMenu";
import SignUpMenu from "../signUpMenu/SignUpMenu";
import RequireAuth from "../../utils/requireAuth";

import './App.css';

const App = () => {
    return (
        <BrowserRouter>
        <div className="App">
          <AppHeader />
          <Routes>
              <Route path='/' element={<RequireAuth> <CatalogPage /> </RequireAuth>} />
              <Route path='/login' element={ <LoginMenu />} />
              <Route path='/register' element={ <SignUpMenu />} />
          </Routes>
        </div>
        </BrowserRouter>
    );
}

export default App;

import React, { useEffect } from 'react';
import AuthProvider from './AuthProvider';

import { BrowserRouter, Routes, Route} from 'react-router-dom';

import NavBar from './Components/NavBar';
import SearchPanel from './Components/SearchPanel';
import ProductSummary from './Components/ProductSummary';

import ProductView from './Views/ProductView';
import LoginView from './Views/LoginView';
import RegisterView from './Views/RegisterView';
import FavouritesView from './Views/FavouritesView';
import ProductViewDetail from './Views/ProductViewDetail';

function App() {

  useEffect(() => {
    document.title = "Comparly"
  },[])
  return (
    <>
    <AuthProvider>
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route path='' element={<SearchPanel/>}/>
          <Route path='/login' element={<LoginView/>}/>
          <Route path='/register' element={<RegisterView/>}/>
          <Route path='/favourites' element={<FavouritesView/>}/>
          <Route path='/product/:productQuery' element={<ProductView/>}/>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
    </>
  );
}

export default App;

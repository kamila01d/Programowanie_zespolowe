import './NavBar.css';
import { useAuth } from "../AuthProvider";
import { Link, useNavigate } from 'react-router-dom';

function NavBar(){

  const authContext = useAuth();
  const navigate = useNavigate();

  let accountBtn = <></>;
  let logoutBtn = <></>;

  if (authContext.isLogged())
  {
    accountBtn = <div className='navbarAccountBtn'></div>;
    logoutBtn = 
    <div className='navbarInlineContainer'>
      <button onClick={() => {authContext.logOut()}} className='navbarLogoutBtn'></button>
    </div>;
  }
  else
  {
    accountBtn = <div className='navbarLoginBtn'></div>;
    logoutBtn = <></>;
  }

    return (
        <div className="navbarContainer">
          <div className='navbarLogoContainer'>
            <Link className='logo' to='/'>
              <div className='navbarLogoWrapper'>
                Comparly
              </div>
            </Link>
          </div>

          <div className='navbarInlineContainer'>
            <Link to='/favourites'>
              <div className='navbarFavouritesBtn'></div>
            </Link>
          </div>

          <div className='navbarInlineContainer'>
            <Link to='/login'>
              {accountBtn}
            </Link>
          </div>

          {logoutBtn}

        </div>
    );
}
/*<div className='navbarDropdownContainer'>
            <div className='navbarDropdownBtn'></div>
          </div>*/

export default NavBar;
import "./FavouritesView.css"
import { useEffect, useState } from 'react';
import "./LoginView.css"
import { useAuth } from "../AuthProvider";
import { Link, json } from 'react-router-dom';

function FavouritesView(){

    const [favouritesArray, setFavouritesArray] = useState([]);
    const authContext = useAuth();

    async function getFavourites(){

        try{

            if(authContext.isLogged())
            {
                let userInfo = await authContext.getUserInfo();
                setFavouritesArray(userInfo.favourites);
            }
            else
            {
                let favouritesArrayStr = localStorage.getItem('favourites');
                if(favouritesArrayStr != null)
                {
                    if(favouritesArrayStr != JSON.stringify(favouritesArray))
                    {
                        console.log(JSON.parse(favouritesArrayStr));
                        setFavouritesArray(JSON.parse(favouritesArrayStr));
                    }
                }
            }

        }
        catch(e)
        {
            console.log(e);
        }

    }

    async function deleteFavourite(product){

        console.log(product);
        try{

            if(authContext.isLogged())
            {
                authContext.deleteFavourite(product);
                getFavourites();
            }
            else
            {
                setFavouritesArray(favouritesArray.filter(prod => prod != product));
                localStorage.setItem('favourites', JSON.stringify(favouritesArray.filter(prod => prod != product)));
            }

        }
        catch(e)
        {
            console.log(e);
        }
    }

    useEffect(() => {
        getFavourites();
    },[]);

    return(
        <div className='favouritesPage'>
            <div className="favouritesContainer">
                <div className="favouritesTitle">Favourite products:</div>
                <div className="favouritesWrapper">
                {favouritesArray.map((product => 
                    
                    <div className='favouritesProductRow'>
                        <Link to={`/product/${product}`}>
                        <div className='favouritesProductName'>{product}</div>
                        </Link>
                        <div className='favouritesProductDeleteBtn' onClick={() => {deleteFavourite(product)}}></div>
                    </div>
                    
                ))}
                </div>
            </div>
        </div>
    );

}

export default FavouritesView;
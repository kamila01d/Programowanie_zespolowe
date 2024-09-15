import { useContext, createContext, useState} from "react";
const AuthContext = createContext();

const AuthProvider = ({ children }) => {

    const [userId, setUserId] = useState(null);
    const [token, setToken] = useState(localStorage.getItem("site") || "");

    const loginAction = async (data) => {

        try {

            //request login token by passing username and password
            const response = await fetch("/users/token", 
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            

            //attempt saving token to state
            const res = await response.json();
            if(res.access_token != undefined) 
            {
                console.log(res);
                console.log(res.access_token);
                setToken(res.access_token);
                localStorage.setItem("site", res.token);
            }
            else
            {
                return (
                    {
                        success: false,
                        message: `${res.detail}`
                    });;
            }

            //request user info
            //await getUserInfo();

            return (
                {
                    success: true,
                    message: ""
                });
        }
        catch (err)
        {
            console.error(err);
            return false;
        }
    };

    const registerAction = async (data) => {

        try{

            const response = await fetch("/users/signup",
                {
                    method: "POST",
                    cache: "no-cache",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                }
            );
    
            const res = await response.json();
            if(res.access_token != undefined) 
            {
                setToken(res.access_token);
                localStorage.setItem("site", res.token);
            }
            else
            {
                return (
                    {
                        success: false,
                        message: `${res.detail}`
                    });
            }

            //request user info
            await getUserInfo();

            return (
                {
                    success: true,
                    message: `${res.detail}`
                });
        }
        catch(err)
        {
            console.log(err);
            return false;
        }

    }

    const getUserInfo = async () => {

        try {

            console.log(token);

            //request user info by token
            const response = await fetch("/users/me", 
            {
                method: "GET",
                headers: {
                    authorization: "Bearer " + token
                }
            });

            //attempt user_id (pk) to userId
            const res = await response.json();
            setUserId(res.pk);
            return res;

        }
        catch (err)
        {
            console.error(err);
        }

    };

    const addFavourite = async (product) => {

        try {

            let payload = {};
            //payload.product_id = product;
            payload.product_id = "testid";
            payload.user_id = `${userId}`;

            //request PUT for userId with token to add product to fav
            const response = await fetch(`/users/favourites/${userId}`, 
            {
                method: "PUT",
                headers: {
                    authorization: "Bearer " + token,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload)
            });

            const res = await response.json();

            return;
           

        }
        catch (err)
        {
            console.error(err);
        }

    }

    const deleteFavourite = async (product) => {

        try {

            let payload = {};
            payload.favouriteProd = product;

            //request PUT for userId with token to add product to fav
            const response = await fetch(`/users/favourites/${userId}`, 
            {
                method: "DELETE",
                headers: {
                    authorization: "Bearer " + token
                },
                body: JSON.stringify(payload)
            });

            const res = await response.json();

            return;
           

        }
        catch (err)
        {
            console.error(err);
        }

    }

    const logOut = () => {
        setUserId(null);
        setToken("");
        localStorage.removeItem("site");
    };

    const isLogged = () => {

        console.log("token");
        console.log(token);
        if(token == "" || token == null)
        {
            return false;
        }
    
        return true;
    }

    return(
        <AuthContext.Provider value={{ token, userId, loginAction, registerAction, logOut, isLogged, addFavourite, deleteFavourite, getUserInfo}}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;

export const useAuth = () => {
  return useContext(AuthContext);
};

import { useEffect, useState } from 'react';
import "./LoginView.css"

import { useAuth } from "../AuthProvider";
import { Link, useNavigate } from 'react-router-dom';

function LoginView()
{
    const authContext = useAuth();
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errorMsg, setErrorMsg] = useState("");

    const handleSubmit = async (event) => {

        event.preventDefault();

        let payload = {};
        payload.username  = username;
        payload.password  = password;

        console.log(payload);

        try{

            let outcome = await authContext.loginAction(payload);
            console.log(outcome);
            if(outcome.success)
            {
                console.log("login successful");
                navigate("/");
            }
            else
            {
                console.log("login unsuccessful");
                setErrorMsg(outcome.message);
            }

        }
        catch(err)
        {
            console.log(err);
        }
        
    }

    useEffect(() => {

        if(authContext.isLogged())
        {
            navigate("/");
        }

    });

    return(
        <>
        <div className="loginviewContainer">
            <div className="loginviewWrapper">
                <div className="loginviewTitle">
                    <div className="loginviewTitleWrapper">
                        Comparly
                    </div>  
                </div>
                <form method="post" className="loginviewForm" onSubmit={(e) => handleSubmit(e)}>

                    <label for="username" className="loginviewLabel">Username/email:</label>
                    <input id="username" value={username} onChange={(e) => setUsername(e.target.value)} className="loginviewInput"></input>

                    <label for="password" className="loginviewLabel">Password:</label>
                    <input type='password' id="password" value={password} onChange={(e) => setPassword(e.target.value)} className="loginviewInput"></input>

                    <button type="submit" className="loginviewSubmit">Login</button>
                    <div className='loginviewErrorMsg'>{`${errorMsg}`}</div>
                </form>
                <div className='loginViewRedirect'>
                    Don't have an account? <Link to="/register">Sign up!</Link> 
                </div>
            </div>
        </div>
        </>
    );

}

export default LoginView;
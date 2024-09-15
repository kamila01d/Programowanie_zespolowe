import { useEffect, useState } from 'react';
import "./RegisterView.css";

import { useAuth } from "../AuthProvider";
import { Link, useNavigate } from 'react-router-dom';

function RegisterView()
{
    const authContext = useAuth();
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [password1, setPassword1] = useState("");
    const [errorMsg, setErrorMsg] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();

        let payload = {};
        payload.username  = username;
        payload.email  = email;
        payload.password  = password;

        if(password != password1)
        {
            setErrorMsg("Passwords do not match");
            return;
        }

        try{

            let outcome = await authContext.registerAction(payload);
            console.log(outcome);
            if(outcome.success)
            {
                navigate("/");
            }
            else
            {
                setErrorMsg(`${outcome.message}`);
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
                <form method="post" className="loginviewForm" onSubmit={handleSubmit}>

                    <label for="username" className="loginviewLabel">Username:</label>
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} id="username" className="loginviewInput"></input>

                    <label for="email" className="loginviewLabel">Email:</label>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} id="email" className="loginviewInput"></input>

                    <label for="password" className="loginviewLabel">Password:</label>
                    <input type='password' id="password" value={password} onChange={(e) => setPassword(e.target.value)} className="loginviewInput"></input>

                    <label for="password1" className="loginviewLabel">Password:</label>
                    <input type='password' id="password1" value={password1} onChange={(e) => setPassword1(e.target.value)} className="loginviewInput"></input>

                    <button type="submit" className="loginviewSubmit">Register</button>
                    <div className='loginviewErrorMsg'>{`${errorMsg}`}</div>

                </form>
                <div className='registerViewRedirect'>
                    Already have an account? <Link href="/login">Sign in!</Link> 
                </div>
            </div>
        </div>
        </>
    );

}

export default RegisterView;
import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

type UserData = {
    email: string;
    password: string;
};

// Login page 
const Login = () =>{
    const navigate = useNavigate();

    const [userData, setUserData] = useState<UserData>({
        email: "",
        password: "",
    })

    const [loginStatus, setLoginStatus] = useState("");

    const updateUserData = (postField: keyof UserData, userInput: string) =>{
        setUserData(prevData => ({
            ...prevData,
            [postField]: userInput
        }))
    }
    
    return(
        <>
            <h1> login </h1>
            <form className="loginForm">
                <div className="inputContainer">
                    <label> Email: </label>
                    <input 
                        type="text" 
                        placeholder="Email"
                        onChange={(e) => updateUserData('email', e.target.value)}
                        required={true}
                    ></input>
                </div>
                <div className="inputContainer">
                    <label> Password: </label>
                    <input 
                        type="password" 
                        placeholder="Password"
                        onChange={(e) => updateUserData('password', e.target.value)}
                    ></input>
                </div>
                
                <button className="subbtn" type="submit"> Login </button>
            </form>

            <div>
                <p> Don't have an account?</p>
                <button className="signupBtn" onClick={()=> navigate("/signup")}> Sign up </button>
            </div>
        </>
    )
}

export default Login
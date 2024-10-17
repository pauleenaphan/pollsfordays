import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";

type UserData = {
    email: string;
    username: string;
    password: string;
    confirmPass: string;
};

// Signup page
const Signup = () =>{
    const navigate = useNavigate();

    const [userData, setUserData] = useState<UserData>({
        email: "",
        username: "",
        password: "",
        confirmPass: "",
    })

    const [signupStatus, setSignupStatus] = useState<string>("");

    const updateUserData = (postField: keyof UserData, userInput: string) =>{
        setUserData(prevData => ({
            ...prevData,
            [postField]: userInput
        }))
    }

    const handleSubmit = (e: FormEvent) =>{
        e.preventDefault();
        const { email, username, password, confirmPass } = userData;

    }

    return(
        <>
            <h1> Signup </h1>
            <form className="signupForm" onSubmit={handleSubmit}>
                <div className="inputContainer">
                    <label> Email: </label>
                    <input 
                        type="email"
                        placeholder="Email"
                        onChange={(e) => updateUserData('email', e.target.value)}
                        required={true}
                    ></input>
                </div>
                <div className="inputContainer">
                    <label> Username: </label>
                    <input 
                        type="text" 
                        placeholder="Name"
                        onChange={(e) => updateUserData('username', e.target.value)}
                        required={true}
                    ></input>
                </div>
                <div className="inputContainer">
                    <label> Password: </label>
                    <input 
                        type="password" 
                        placeholder="Password"
                        onChange={(e) => updateUserData('password', e.target.value)}
                        required={true}
                    ></input>
                </div>
                <div className="inputContainer">
                    <label> Confirm Password: </label>
                    <input 
                        type="password" 
                        placeholder="Confirm Password"
                        onChange={(e) => updateUserData('confirmPass', e.target.value)}
                        required={true}
                    ></input>
                </div>
                <button className="signupBtn" type="submit"> Signup </button>
            </form>

            <div>
                <p> Already have an account? </p>
                <button className="loginBtn" onClick={() => navigate("/login")}> Login </button>
            </div>
        </>
    )
}

export default Signup
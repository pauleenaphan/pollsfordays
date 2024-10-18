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

    const handleSubmit = async (e: FormEvent) =>{
        e.preventDefault();
        const { email, username, password } = userData;
    
        if(password !== userData.confirmPass){
            setSignupStatus("Passwords don't match");
            return;
        }
    
        try{
            const signupResponse = await fetch("http://localhost:8000/api/signup/", {
                method: "POST",
                headers:{
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, username, password })
            });
    
            if(signupResponse.ok){
                // Now log the user in immediately after signup
                const loginResponse = await fetch("http://localhost:8000/api/login/", {
                    method: "POST",
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ email, password }) // Use the same email and password
                });
    
                if(loginResponse.ok){
                    const data = await loginResponse.json(); // Get the token from the response
                    localStorage.setItem("token", data.token); 
                    localStorage.setItem("isLoggedIn", "true");
                    alert("User signed up and logged in!");
                    navigate("/homepage");
                }else{
                    const loginError = await loginResponse.json();
                    setSignupStatus(loginError.detail || "Login failed");
                }
            }else{
                const signupError = await signupResponse.json();
                setSignupStatus(signupError.detail || "Signup failed");
            }
        }catch(error){
            console.error("Error signing up", error);
        }
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
            <p> {signupStatus} </p>

            <div>
                <p> Already have an account? </p>
                <button className="loginBtn" onClick={() => navigate("/login")}> Login </button>
            </div>
        </>
    )
}

export default Signup
import { useNavigate } from "react-router-dom";

// Welcome page where user can login or signup
const Loggedout = () =>{
    const navigate = useNavigate();

    return(
        <>
            <h1> PollsForDays</h1>
            <p> Would you rather login or signup? </p>
            <button onClick={() =>{navigate("/login")}}> Login </button>
            <button onClick={() =>{navigate("/signup")}}> Signup </button>
            <p> Author: Pauleena Phan </p>
            <p> Date posted: 10/15/2024 </p>
        </>
    )
}

export default Loggedout
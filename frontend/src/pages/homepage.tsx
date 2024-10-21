import Modal from "../components/modal";
import { FormEvent, useState, useEffect } from "react";

function getFormattedDate(): string {
    const today = new Date();
    const day = String(today.getDate()).padStart(2, '0'); // Get the day and pad it to 2 digits
    const month = String(today.getMonth() + 1).padStart(2, '0'); // Get the month (0-indexed) and pad to 2 digits
    const year = today.getFullYear(); // Get the full year

    return `${month}/${day}/${year}`; // Return the date in MM/DD/YYYY format
}

type PollData = {
    title: string,
    options: string[],
    timeLimit: number
};

type Poll = {
    title: string,
    options: string[],
    timeLimit: number,
    author: string,
    datePosted: string
}

type PollList = Poll[];

// Homepage of all the polls
const Homepage = () =>{
    const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
    const [pollData, setPollData] = useState<PollData>({ // Poll created by user
        title: "",
        options: ["", ""],
        timeLimit: 0
    })

    const [pollList, setPollList] = useState<PollList>([]);

    const toggleNewPollModal = () => {
        setIsModalOpen(!isModalOpen); 
    };

    // Function to handle poll data changes
    const handlePollChange = (field: string, value: any) => {
        setPollData((prevState) => ({
            ...prevState,
            [field]: value, 
        }));
    };

    // Function to add another option to the poll (max 6 choices)
    const addOption = () => {
        if (pollData.options.length < 6) { // Max 6 options
            handlePollChange("options", [...pollData.options, ""]); // Add a new empty option
        }
    };

    // Function to handle input change for each option
    const handleOptionChange = (index: number, newOption: string) => {
        const updatedOptions = [...pollData.options];
        updatedOptions[index] = newOption; // Update the specific option
    
        handlePollChange("options", updatedOptions); // Update options array
    };

    // Get all Polls
    const fetchAllPolls = async () =>{
        try{
            const response = await fetch("http://localhost:8000/api/pollmodels/getAllPolls", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            if(response.ok){
                const data: PollList = await response.json(); // Correctly parse the JSON response
                setPollList(data); 
                console.log(pollList[0]);
            }
        }catch(error){ console.error("Error getting all polls", error) }
    }

    // Create new Polls
    const createPoll = async (e: FormEvent) =>{
        e.preventDefault();
        console.log(localStorage.getItem("token"));
        const { title, options, timeLimit } = pollData;
        try{
            const response = await fetch("http://localhost:8000/api/pollmodels/create/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem("token")}`
                },
                body: JSON.stringify({ title, choices: options, author: localStorage.getItem("username"), timeLimit, datePosted: getFormattedDate() })
            })
            console.log(response["body"]);
            if(response.ok){
                alert("poll has been created")
                // refresh poll page
                toggleNewPollModal();
                setPollData({
                    title: "",
                    options: ["", ""], 
                    timeLimit: 0 
                });
            }
        }catch(error){ console.error("Error creating poll", error) }
    }

    useEffect(() => {
        fetchAllPolls();
    }, []);

    return(
        <>
            all polls here
            <button onClick={toggleNewPollModal}> new poll </button>
            {pollList.map((poll, index) =>(
                <li key={index}>
                    <h3>{poll.title}</h3>
                    <p>Options:</p>
                    <p>{poll.options} </p>
                    {/* <ul>
                        {poll.options.map((option, optionIndex) => (
                            <li key={optionIndex}>{option}</li>
                        ))}
                    </ul> */}
                    <p>Time Limit: {poll.timeLimit} hours</p>
                    <p>Author: {poll.author}</p>
                    <p>Date Posted: {poll.datePosted}</p>
                </li>
            ))}

            <Modal isOpen={isModalOpen} onClose={toggleNewPollModal} title="New Poll">
                <form className="newPollForm" onSubmit={createPoll}>
                    <label> Question </label>
                    <textarea 
                        required 
                        placeholder="Write your question here"
                        onChange={(e) => handlePollChange("title", e.target.value)} // Update title
                        ></textarea>

                    <div>
                        <p> Options (Maximum of 6 choices) </p>
                        {pollData.options.map((option, index) => (
                            <div key={index} className="option-input">
                                <textarea
                                    value={option}
                                    onChange={(e) => handleOptionChange(index, e.target.value)}
                                    placeholder={`Option ${index + 1}`}
                                    required={index < 2}
                                />
                            </div>
                        ))}
                        <button onClick={addOption}>Add Option</button>
                    </div>

                    <label> Time Limit </label>
                    <input 
                        type="number" 
                        required
                        placeholder="Hours"
                        onChange={(e) => handlePollChange("timeLimit", e.target.value)} // Update title
                        ></input>

                    <button> Post Poll </button>
                </form>
            </Modal>
        </>
    )
}

export default Homepage
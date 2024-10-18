import Modal from "../components/modal";
import { useState } from "react";

// Homepage of all the polls
const Homepage = () =>{
    const [isModalOpen, setIsModalOpen] = useState<boolean>(false);

    const toggleModal = () => {
        setIsModalOpen(!isModalOpen); 
    };


    return(
        <>
            all polls here
            <button onClick={toggleModal}> new poll </button>

            <Modal isOpen={isModalOpen} onClose={toggleModal} title="My Modal Title">
                <p>This is the content of the modal.</p>
                <p>You can add anything here!</p>
            </Modal>
        </>
    )
}

export default Homepage
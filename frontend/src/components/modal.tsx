import React from 'react';
import "../styles/modal.css";

interface ModalProps {
    isOpen: boolean; // Indicates if the modal is open
    onClose: () => void; // Function to close the modal
    title: string; // Title of the modal
    children: React.ReactNode; // Content of the modal
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, title, children }) => {
    if (!isOpen) return null; // Don't render the modal if it's not open

    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <div className="modal-header">
                    <h2>{title}</h2>
                    <button onClick={onClose} className="close-button">
                        &times;
                    </button>
                </div>
                <div className="modal-body">
                    {children} {/* Render any children passed to the modal */}
                </div>
                {/* <div className="modal-footer">
                    <button onClick={onClose} className="footer-button">Close</button>
                </div> */}
            </div>
        </div>
    );
};

export default Modal;
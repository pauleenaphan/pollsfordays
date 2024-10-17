import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Loggedout from './pages/loggedout';
import Login from "./pages/login";
import Signup from './pages/signup';
import Homepage from './pages/homepage';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/loggedout" element={<Loggedout/>}/>
          <Route path="/homepage" element={<Homepage/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/signup" element={<Signup/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App

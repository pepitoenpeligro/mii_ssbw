
import './Dashboard.css'

import React, { Component } from "react";
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';
import Senderos from '../Senderos/Senderos';

const Dashboard = () => {



    return (
        <div>
            <Navbar />

            <Senderos/>
            <Footer></Footer>

            
            
        </div>


    );

}


export default Dashboard;
import React, { Component } from "react";
import { Link } from "react-router-dom";
import './Navbar.css'

class Navbar extends Component {

    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <a className="navbar-brand" href="#">Senderos Home</a>
                    <div className="collapse navbar-collapse" id="navbarTogglerDemo03">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item ">
                                <a className="nav-link" href="#">Login</a>
                            </li>
                            <li className="nav-item ">
                                <a className="nav-link" href="#" tabindex="-1" >Logout</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        )


    }



}


export default Navbar;
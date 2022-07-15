import React, { Component } from "react";

// Stateless Functional Component
const NavBar = ({ totalCounters }) => {
  console.log("Navbar - Rendered");
  return (
    <nav className="navbar bg-light">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          Navbar
          <span className="badge badge-pill badge-secondary">
            {totalCounters}
          </span>
        </a>
      </div>
    </nav>
  );
};

// class NavBar extends Component {
//   render() {

//   }
// }

export default NavBar;

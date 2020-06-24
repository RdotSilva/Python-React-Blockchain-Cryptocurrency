import React from "react";
import { Nav } from "react-bootstrap";

function Navbar() {
  return (
    <Nav fill variant="tabs" defaultActiveKey="/">
      <Nav.Item>
        <Nav.Link href="/">Home</Nav.Link>
      </Nav.Item>
    </Nav>
  );
}

export default Navbar;

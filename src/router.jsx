import React from "react";
import { Route, Routes } from "react-router-dom";
import HomePage from "./Components/home";
import Book from "./Components/book";
import Register from "./Components/register";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/book" element={<Book />} />
      <Route path="/join" element={<Register />} />
      <Route path="/*" element={<HomePage />} />
    </Routes>
  );
};

export default AppRoutes;

import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "./pages/Login";

import { Provider } from "react-redux";
import store from "./store";

import "bootstrap-css-only/css/bootstrap.min.css";

import "./App.css";




function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <Router>
          <Route exact path="/login" component={Login} />
        </Router>
      </div>
    </Provider>
  );
}

export default App;

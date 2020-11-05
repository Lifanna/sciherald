import React from "react";
import CssBaseline from "@material-ui/core/CssBaseline";
import { Header } from "./components/Header";
import { Main } from "./components/Main";
import { Footer } from "./components/Footer";
import { BrowserRouter } from "react-router-dom";
import { Provider } from "react-redux";
import { store } from "./store";

export default function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <React.Fragment>
          <CssBaseline />
          <Header />
          <Main />
          <Footer />
        </React.Fragment>
      </BrowserRouter>
    </Provider>
  );
}

import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import { Header } from "./components/Header";
import { Main } from "./components/Main";
import { Footer } from "./components/Footer";
import { BrowserRouter } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  mainGrid: {
    marginTop: theme.spacing(3),
  },
}));

export default function App() {
  const classes = useStyles();

  return (
      <BrowserRouter>
        <React.Fragment>
          <CssBaseline />
          <Header/>
          <Main />
          <Footer />
        </React.Fragment>
      </BrowserRouter>
  );
}

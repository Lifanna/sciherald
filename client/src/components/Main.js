import { Container, Grid, makeStyles } from "@material-ui/core";
import React from "react";
import { Route, Switch } from "react-router-dom";
import { ArticlePage } from "../pages/ArticlePage";
import { HomePage } from "../pages/HomePage";
import { Sidebar } from "./Sidebar";



const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: "1rem",
  },
}));

export const Main = () => {
  const classes = useStyles();
  return (
    <Container className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={8}>
          <Switch>
          <Route path="/articles/:id" exact>
          <ArticlePage/>
            
          </Route>
          <Route path="/" exact>
          <HomePage/>
            
          </Route>
          </Switch>
        </Grid>
        <Grid item xs={4}>
          <Sidebar />
        </Grid>
      </Grid>
    </Container>
  );
};

import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import ThumbUpIcon from "@material-ui/icons/ThumbUp";
import CommentIcon from "@material-ui/icons/Comment";
import { useHistory } from "react-router-dom";
const useStyles = makeStyles({
  root: {
    marginBottom: "1rem",
    width: "100%",
  },
});

export function Article({ title, description, id }) {
  const classes = useStyles();
  const { push } = useHistory();
  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardContent onClick={() => push(`/articles/${id}`)}>
          <Typography gutterBottom variant="h5" component="h2">
            {title}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            {description}
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions style={{ marginLeft: "15px" }}>
        <ThumbUpIcon fontSize="small" />
        <CommentIcon fontSize="small" />
      </CardActions>
    </Card>
  );
}

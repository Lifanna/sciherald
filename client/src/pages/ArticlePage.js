import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { red } from "@material-ui/core/colors";
import FavoriteIcon from "@material-ui/icons/Favorite";
import ShareIcon from "@material-ui/icons/Share";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import { featuredPosts } from "../constants";
import { useDispatch, useSelector } from "react-redux";
import { articleLoadRequestAction } from "../store/articleList";
import { CircularProgress } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
  root: {
    maxWidth: "100%",
    marginBottom: "1rem",
  },
  media: {
    height: 0,
    paddingTop: "56.25%", // 16:9
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
  avatar: {
    backgroundColor: red[500],
  },
}));

export const ArticlePage = () => {
  const { id } = useParams();
  const classes = useStyles();

  const { currentArticle: article, error, isLoading } = useSelector(state => ({
    currentArticle: state.articleList.currentArticle,
    error: state.articleList.errors.currentArticle,
    isLoading: state.articleList.loadings.currentArticle,
  }));

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(articleLoadRequestAction(id));
  }, [dispatch, articleLoadRequestAction, id]);
  const circular = isLoading && <CircularProgress size={100} />;
  const articlesJSX = !isLoading && !error && (
    <Card className={classes.root}>
      <CardHeader
        avatar={
          <Avatar aria-label="recipe" className={classes.avatar}>
            R
          </Avatar>
        }
        action={
          <IconButton aria-label="settings">
            <MoreVertIcon />
          </IconButton>
        }
        title={article && article.title}
        subheader="September 14, 2016"
      />
      <CardMedia
        className={classes.media}
        image="./google1592906914390.jpg"
        title="Paella dish"
      />
      <CardContent>
        <Typography variant="body2" color="textSecondary" component="p">
          {article && article.body}
        </Typography>
      </CardContent>

      <CardActions disableSpacing>
        <IconButton aria-label="add to favorites">
          <FavoriteIcon />
        </IconButton>
        <IconButton aria-label="share">
          <ShareIcon />
        </IconButton>
      </CardActions>
    </Card>
  );
  const errorJSX = error && <Typography variant="h6">{error}</Typography>;

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        minHeight: "80vh",
        alignItems: "center",
        width: "100%",
      }}
    >
      {circular}
      {errorJSX}
      {articlesJSX}
    </div>
  );
};

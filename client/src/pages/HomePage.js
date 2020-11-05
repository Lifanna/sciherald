import { CircularProgress, Typography } from "@material-ui/core";
import React from "react";
import { useSelector } from "react-redux";
import { Article } from "../components/Article";

export const HomePage = () => {
  const { articles, isLoading, error } = useSelector(
    state => state.articleList
  );

  const circular = isLoading && <CircularProgress size={100} />;
  const articlesJSX =
    !isLoading &&
    !error &&
    articles.map((post, id) => {
      return (
        <Article
          id={id}
          title={post.title}
          description={post.description}
          key={post.title}
        />
      );
    });
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

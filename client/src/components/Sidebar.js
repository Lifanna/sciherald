import { Button, CircularProgress, Paper, Typography } from "@material-ui/core";
import React from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";

const sections = ["Недавние публикаций", "Топ статей", "Топ тематик"];

export const Sidebar = () => {
  const { articles, error, isLoading } = useSelector(state => ({
    articles: state.articleList.articles,
    error: state.articleList.errors.articles,
    isLoading: state.articleList.loadings.articles,
  }));
  const sidebarArticles = [
    articles.slice(0, 5),
    articles.slice(6, 11),
    articles.slice(11, 16),
  ];
  return (
    <>
      {sections.map((section, idx) => {
        return (
          <SideBarSection
            isLoading={isLoading}
            key={section}
            title={section}
            items={sidebarArticles[idx]}
          />
        );
      })}
    </>
  );
};

const SideBarSection = ({ title, items, isLoading }) => {
  if (isLoading) {
    return (
      <Paper
        style={{
          padding: "1rem",
          marginBottom: "1rem",
          minHeight: "200px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexDirection: "column",
        }}
      >
        {title}
        <CircularProgress size={100} />
      </Paper>
    );
  }
  return (
    <Paper
      style={{
        padding: "1rem",
        marginBottom: "1rem",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      {title}
      {items.map(item => {
        return (
          <Button key={item.id} component={NavLink} to={`/articles/${item.id}`}>
            {item.title.slice(0, 15)}
          </Button>
        );
      })}
    </Paper>
  );
};

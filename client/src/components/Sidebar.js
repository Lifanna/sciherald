import { Paper, Typography } from "@material-ui/core";
import React from "react";

const sections = ["Недавние публикаций", "Топ статей", "Топ тематик"];

export const Sidebar = ({ title }) => {
  return (
    <>
      {sections.map((section) => {
        return (
          <Paper>
            <Typography variant="h5" gutterBottom>
              {section}
              {new Array(4).fill("").map((_, index) => {
                return (
                  <Typography variant={"h6"}>{`News ${index}`}</Typography>
                );
              })}
            </Typography>
          </Paper>
        );
      })}
    </>
  );
};

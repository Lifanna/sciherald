import { Paper, Typography } from "@material-ui/core";
import React from "react";

const sections = ["Недавние публикаций", "Топ статей", "Топ тематик"];

export const Sidebar = ({ title }) => {
  return (
    <>
      {sections.map(section => {
        return (
          <Paper
            key={section}
            style={{ padding: "1rem", marginBottom: "1rem" }}
          >
            <Typography variant="h5" gutterBottom>
              {section}
              {new Array(4).fill("").map((_, index) => {
                return (
                  <Typography
                    key={index}
                    variant={"h6"}
                  >{`News ${index}`}</Typography>
                );
              })}
            </Typography>
          </Paper>
        );
      })}
    </>
  );
};

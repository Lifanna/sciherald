import { createAction, createSlice } from "@reduxjs/toolkit";

const initialState = {
  articles: [],
  currentArticle: null,
  errors: {
    articles: null,
    currentArticle: null,
  },
  loadings: {
    articles: false,
    currentArticle: false,
  },
};

export const articleListSlice = createSlice({
  name: "articleList",
  initialState,
  reducers: {
    articlesRequest(state, action) {
      const { type } = action.payload;
      state.loadings[type] = true;
    },
    articlesLoad(state, action) {
      const { type, data } = action.payload;
      state[type] = data;
      state.errors[type] = null;
      state.loadings[type] = false;
    },
    articlesError(state, action) {
      const { type, data } = action.payload;
      state.loadings[type] = false;
      state.errors[type] = data;
    },
  },
});

const {
  articlesRequest,
  articlesLoad,
  articlesError,
} = articleListSlice.actions;

export const articlesRequestAction = () =>
  articlesRequest({ type: "articles" });
export const articlesLoadAction = data =>
  articlesLoad({ type: "articles", data });
export const articlesErrorAction = () => articlesError({ type: "articles" });

export const articleRequestAction = () =>
  articlesRequest({ type: "currentArticle" });
export const articleLoadAction = data =>
  articlesLoad({ type: "currentArticle", data });
export const articleErrorAction = () =>
  articlesError({ type: "currentArticle" });

export const articlesLoadRequestAction = createAction("FETCH_ARTICLES_REQUEST");
export const articleLoadRequestAction = createAction("FETCH_ARTICLE_REQUEST");

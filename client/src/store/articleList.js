import { createAction, createSlice } from "@reduxjs/toolkit";

const initialState = {
  articles: [],
  error: null,
  isLoading: false,
};

export const articleListSlice = createSlice({
  name: "articleList",
  initialState,
  reducers: {
    articlesRequest(state) {
      state.isLoading = true;
    },
    articlesLoad(state, action) {
      state.articles = action.payload;
      state.error = null;
      state.isLoading = false;
    },
    articlesError(state, action) {
      state.isLoading = false;
      state.error = action.payload;
    },
  },
});

export const articlesLoadRequestAction = createAction("FETCH_ARTICLES_REQUEST");

export const {
  articlesRequest: articlesRequestAction,
  articlesLoad: articlesLoadAction,
  articlesError: articlesErrorAction,
} = articleListSlice.actions;

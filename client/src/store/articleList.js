import { createAction, createSlice } from "@reduxjs/toolkit";
import { all, call, put, takeEvery } from "redux-saga/effects";

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
      state.loading = true;
    },
    articlesLoad(state, action) {
      state.articles = action.payload;
      state.error = null;
      state.loading = false;
    },
    articlesError(state, action) {
      state.loading = false;
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

export function* fetchArticlesSaga() {
  yield put(articlesRequestAction());
  try {
    const articles = yield call();

    yield put(articlesLoadAction(articles));
  } catch (error) {
    yield put(articlesErrorAction(error.message));
  }
}

export const saga = function* () {
  yield all([
    takeEvery(articlesLoadRequestAction.type, fetchArticlesSaga),
    // takeEvery(bookAddRequestAction.type, addBookSaga),
  ]);
};

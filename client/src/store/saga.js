import { put, spawn, takeEvery, all, call } from "redux-saga/effects";
import {
  articlesErrorAction,
  articlesLoadAction,
  articlesRequestAction,
  articlesLoadRequestAction,
  articleLoadAction,
  articleErrorAction,
  articleLoadRequestAction,
  articleRequestAction,
} from "./articleList";
import { getArticleById, getArticles } from "../services/api-service";

export function* fetchArticlesSaga() {
  yield put(articlesRequestAction());
  try {
    const articles = yield call(getArticles);
    yield put(articlesLoadAction(articles));
  } catch (error) {
    yield put(articlesErrorAction({ type: "articles" }));
  }
}

export function* fetchArticle({ payload }) {
  yield put(articleRequestAction());
  try {
    const article = yield call(getArticleById, payload);

    yield put(articleLoadAction(article));
  } catch (error) {
    yield put(articleErrorAction(error.message));
  }
}

export const artilcleListSaga = function* () {
  yield all([
    takeEvery(articlesLoadRequestAction.type, fetchArticlesSaga),
    takeEvery(articleLoadRequestAction.type, fetchArticle),
  ]);
};

export default function* () {
  yield spawn(artilcleListSaga);
}

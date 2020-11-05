import { call, put, spawn, delay, takeEvery, all } from "redux-saga/effects";
import {
  articlesErrorAction,
  articlesLoadAction,
  articlesRequestAction,
  articlesLoadRequestAction,
} from "./articleList";
import axios from "axios";
import { featuredPosts } from "../constants";

export function* fetchArticlesSaga() {
  yield put(articlesRequestAction());
  try {
    // const res = yield call(
    //   axios.get("https://sciherald.herokuapp.com/api/v1/get-articles")
    // );
    // const articles = res.data;
    // yield put(articlesLoadAction(featuredPosts));

    yield delay(1000);

    if (true) {
      yield put(articlesLoadAction(featuredPosts));
    } else {
      yield put(articlesErrorAction("Ошибка"));
    }
  } catch (error) {
    yield put(articlesErrorAction(error.message));
  }
}

export const artilcleListSaga = function* () {
  yield all([takeEvery(articlesLoadRequestAction.type, fetchArticlesSaga), ,]);
};

export default function* () {
  yield spawn(artilcleListSaga);
}

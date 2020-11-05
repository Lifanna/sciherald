import { spawn } from "redux-saga/effects";
import { saga as artilcleListSaga } from "./articleList";

export default function* () {
  yield spawn(artilcleListSaga);
}

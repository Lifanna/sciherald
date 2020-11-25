import Axios from "axios";

const axiosInstance = Axios.create({
  baseURL: "https://jsonplaceholder.typicode.com/",
});

const resourcesMap = {
  articles: "posts",
  article: id => {
    return `${resourcesMap.articles}/${id}`;
  },
};

export async function getArticles() {
  const res = await axiosInstance.get(resourcesMap.articles);
  return res.data;
}
export async function getArticleById(id) {
  const url = resourcesMap.article(id);
  const res = await axiosInstance.get(url);
  return res.data;
}

import Axios from "axios";

const axiosInstance = Axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
});

const resourcesMap = {
  articles: "articles",
  article: (id) => {
    return `${resourcesMap.articles}/${id}`;
  },
  image: (id) => `images/${id}`,
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

export async function getImagesById(id) {
  const url = resourcesMap.image(id);
  const res = await axiosInstance.get(url);
  return res.data;
}

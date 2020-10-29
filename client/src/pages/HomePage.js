import React from 'react'
import { Article } from '../components/Article';
import { featuredPosts } from '../constants';

export const HomePage = () => {
  
  return (
    <>
      {featuredPosts.map((post, id) => {
            return (
              <Article
                id={id}
                title={post.title}
                description={post.description}
                key={post.title}
              />
            );
          })}
    </>
  )
}

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


user_data = {
    'User': ['A', 'B', 'C', 'D', 'E'],
    'Ae Dil Hai Mushkil': [5, 4, 0, 0, 3],
    'Enthiran': [3, 0, 2, 4, 0],
    'velaiilla pattadhari': [4, 5, 0, 3, 0],
    'zindagi na milegi dobara': [0, 2, 4, 5, 4],
    'The Greatest of All Time': [0, 0, 5, 3, 2],
}

movie_data = {
    'Movie': ['Naanum Rowdy Dhaan', 'Ae Dil Hai Mushkil', 'Enthiran', 'zindagi na milegi dobara', 'The Greatest of All Time'],
    'Genres': ['Action|Comedy', 'Drama|Romance', 'Action|Sci-Fi', 'Comedy|Drama', 'Sci-Fi|Thriller']
}


user_df = pd.DataFrame(user_data).set_index('User')
movies_df = pd.DataFrame(movie_data)


user_df = user_df.rename(columns={'velaiilla pattadhari': 'Velaiilla Pattadhari', 'Ae Dil Hai Mushkil': 'Ae Dil Hai Mushkil', 'Enthiran': 'Enthiran', 'zindagi na milegi dobara': 'zindagi na milegi dobara', 'The Greatest of All Time': 'The Greatest of All Time'})
movies_df = movies_df.rename(columns={'Movie': 'Movie'})


user_similarity = cosine_similarity(user_df.fillna(0))
user_similarity_df = pd.DataFrame(user_similarity, index=user_df.index, columns=user_df.index)

def get_collaborative_recommendations(user, top_n=3):
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]
    similar_users_ratings = user_df.loc[similar_users].mean(axis=0)
    user_ratings = user_df.loc[user]
    
    recommendations = similar_users_ratings - user_ratings
    recommendations = recommendations[recommendations > 0].sort_values(ascending=False)
    
    return recommendations.head(top_n).index.tolist()


vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split('|'))
tfidf_matrix = vectorizer.fit_transform(movies_df['Genres'])

def get_content_recommendations(user_preferences, top_n=3):
    user_vector = vectorizer.transform([user_preferences])
    cosine_similarities = linear_kernel(user_vector, tfidf_matrix).flatten()
    movies_df['Similarity'] = cosine_similarities
    return movies_df.sort_values(by='Similarity', ascending=False).head(top_n)['Movie'].tolist()


user = 'C'
user_preferences = 'Action|Sci-Fi'

collab_recs = get_collaborative_recommendations(user)
content_recs = get_content_recommendations(user_preferences)

print(f"Collaborative Filtering Recommendations for User {user}: {collab_recs}")
print(f"Content-Based Recommendations for Preferences '{user_preferences}': {content_recs}")

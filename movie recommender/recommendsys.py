import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
# Replace 'C:\\path\\to\\u.data' and 'C:\\path\\to\\u.item' with the actual paths to your files
ratings = pd.read_csv(r"C:\Users\satya\OneDrive\Desktop\movie recommender\ml-100k\u.data", sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv(r"C:\Users\satya\OneDrive\Desktop\movie recommender\ml-100k\u.item", sep='|', names=['movie_id', 'title'], usecols=[0, 1], encoding='latin-1')

# Merge the datasets on the movie_id
data = pd.merge(ratings, movies, on='movie_id')

# Create the user-item matrix
user_item_matrix = data.pivot_table(index='user_id', columns='title', values='rating')

# Fill NaN values with 0
user_item_matrix = user_item_matrix.fillna(0)

# Compute the cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert the similarity matrix to a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get recommendations for a user
def get_recommendations(user_id, n_recommendations=5):
    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    
    # Get movies rated by similar users
    similar_user_ratings = user_item_matrix.loc[similar_users.index]
    
    # Weighted average of movie ratings by similar users
    weighted_ratings = np.dot(similar_users.values, similar_user_ratings)
    
    # Normalize ratings
    weighted_ratings = weighted_ratings / np.array([np.abs(similar_users.values).sum()])
    
    # Create a Series with movie ratings
    movie_recommendations = pd.Series(weighted_ratings, index=user_item_matrix.columns)
    
    # Filter out movies already rated by the user
    movie_recommendations = movie_recommendations[user_item_matrix.loc[user_id] == 0]
    
    # Sort by rating and get top n recommendations
    top_recommendations = movie_recommendations.sort_values(ascending=False).head(n_recommendations)
    
    return top_recommendations

# Example usage: Get recommendations for user with ID 1
user_id = 1
recommendations = get_recommendations(user_id)
print(f"Recommendations for User {user_id}:")
for movie, rating in recommendations.items():
    print(f"{movie}: {rating:.2f}")

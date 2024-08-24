import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Sample data: User ratings for movies
data = {
    'User': ['User1', 'User1', 'User1', 'User2', 'User2', 'User2', 'User3', 'User3', 'User3'],
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie1', 'Movie2', 'Movie4', 'Movie2', 'Movie3', 'Movie4'],
    'Rating': [5, 3, 4, 4, 2, 5, 5, 4, 1]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Pivot the data to create a user-item matrix
user_item_matrix = df.pivot_table(index='User', columns='Movie', values='Rating')

# Fill NaN values with 0
user_item_matrix = user_item_matrix.fillna(0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert similarity matrix to DataFrame for easier handling
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get recommendations for a user
def get_recommendations(user, n_recommendations=2):
    # Find similar users
    similar_users = user_similarity_df[user].sort_values(ascending=False)
    
    # Get movies rated by similar users
    similar_user_ratings = user_item_matrix.loc[similar_users.index]
    
    # Weighted average of movie ratings by similar users
    weighted_ratings = np.dot(similar_users.values, similar_user_ratings)
    
    # Normalize ratings
    weighted_ratings = weighted_ratings / np.array([np.abs(similar_users.values).sum()])
    
    # Create a Series with movie ratings
    movie_recommendations = pd.Series(weighted_ratings, index=user_item_matrix.columns)
    
    # Filter out movies already rated by the user
    movie_recommendations = movie_recommendations[user_item_matrix.loc[user] == 0]
    
    # Sort by rating and get top n recommendations
    top_recommendations = movie_recommendations.sort_values(ascending=False).head(n_recommendations)
    
    return top_recommendations

# Example usage
user = 'User1'
recommendations = get_recommendations(user)
print(f"Recommendations for {user}:\n{recommendations}")

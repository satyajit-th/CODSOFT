How It Works:
Data Preparation: The code starts with a small dataset of user ratings for different movies.
User-Item Matrix: The data is converted into a user-item matrix where each row represents a user, each column represents a movie, and the values represent the ratings.
Cosine Similarity: Cosine similarity is calculated between users to identify similar users based on their movie ratings.
Recommendation Function: The get_recommendations function identifies similar users, aggregates their ratings, and recommends movies to the target user that they haven't rated yet.
You can modify the dataset and add more users, movies, and ratings to see how the recommendations change.
Overview
This system uses collaborative filtering to recommend movies to users based on the MovieLens 100k dataset. Collaborative filtering works by identifying users with similar preferences and recommending items (in this case, movies) that those similar users have liked.

Steps Breakdown
Loading the Data:

Ratings Data: The u.data file contains user ratings for movies. Each line includes a user_id, movie_id, rating, and timestamp.
Movies Data: The u.item file contains movie information, such as movie_id and title. This file is used to map movie IDs to movie titles.
python
Copy code
ratings = pd.read_csv('C:\\path\\to\\u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv('C:\\path\\to\\u.item', sep='|', names=['movie_id', 'title'], usecols=[0, 1], encoding='latin-1')
Merging the Data:

The ratings data and movie data are merged using movie_id. This allows us to associate each rating with the corresponding movie title.

python

data = pd.merge(ratings, movies, on='movie_id')
Creating the User-Item Matrix:

The data is reshaped into a user-item matrix where each row represents a user, each column represents a movie, and the values are the ratings given by the user to the movie.
If a user hasn’t rated a movie, that position in the matrix is filled with 0.

python

user_item_matrix = data.pivot_table(index='user_id', columns='title', values='rating').fillna(0)
Calculating User Similarity:

The system calculates the similarity between users using cosine similarity. Cosine similarity measures the cosine of the angle between two vectors—in this case, the vectors are rows in the user-item matrix representing users.
The result is a user similarity matrix, where each entry (i, j) represents how similar user i is to user j.

python

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
Making Recommendations:

Finding Similar Users: For the target user (e.g., user_id = 1), the system identifies other users who have similar tastes by sorting the similarity scores in descending order.
Aggregating Ratings: The system then looks at the ratings given by these similar users to movies the target user hasn’t rated. It computes a weighted average of these ratings, where the weights are the similarity scores.
Filtering and Sorting: Movies that the target user has already rated are excluded, and the remaining movies are sorted by their aggregated scores. The top n movies are recommended.

python

similar_users = user_similarity_df[user_id].sort_values(ascending=False)
similar_user_ratings = user_item_matrix.loc[similar_users.index]
weighted_ratings = np.dot(similar_users.values, similar_user_ratings)
weighted_ratings = weighted_ratings / np.array([np.abs(similar_users.values).sum()])
movie_recommendations = pd.Series(weighted_ratings, index=user_item_matrix.columns)
movie_recommendations = movie_recommendations[user_item_matrix.loc[user_id] == 0]
top_recommendations = movie_recommendations.sort_values(ascending=False).head(n_recommendations)
Output:

The system prints the top movie recommendations for the user, excluding the dtype information for clarity.

python


print(f"Recommendations for User {user_id}:")
for movie, rating in recommendations.items():
    print(f"{movie}: {rating:.2f}")
Example Output
If you run the system for user_id = 1, the output might look like this:


Recommendations for User 1:
Star Wars (1977): 4.87
Raiders of the Lost Ark (1981): 4.75
Pulp Fiction (1994): 4.67
...
How It Helps
Personalized: Recommendations are personalized based on the preferences of users similar to the target user.
Scalable: This collaborative filtering approach can scale to handle larger datasets, though more sophisticated algorithms may be needed for very large datasets.
Flexible: You can adjust the number of recommendations, similarity metric, or even extend the system to include more complex features like item-based filtering or hybrid models.
This system provides a basic yet effective way to recommend items in various applications beyond movies, such as books, music, or even products.







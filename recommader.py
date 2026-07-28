import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genre into vectors
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies["genre"])

# Calculate similarity
similarity = cosine_similarity(count_matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    for i in range(len(movies)):
        if movies.iloc[i]["title"].lower() == movie_name:
            scores = list(enumerate(similarity[i]))
            scores = sorted(scores, key=lambda x: x[1], reverse=True)

            recommendations = []
            for movie in scores[1:6]:
                recommendations.append(movies.iloc[movie[0]]["title"])

            return recommendations

    return ["Movie not found"]

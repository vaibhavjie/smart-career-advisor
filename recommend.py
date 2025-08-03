from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from career_data import career_data

def recommend_careers(user_input):
    all_career_texts = []
    for job in career_data:
        all_text = job["career"] + " " + " ".join(job["skills"]) + " " + job["description"]
        all_career_texts.append(all_text)

    all_career_texts.append(user_input)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_career_texts)

    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

    top_indices = similarity_scores.argsort()[::-1][:3]

    results = []
    for idx in top_indices:
        results.append({
            "career": career_data[idx]["career"],
            "description": career_data[idx]["description"],
            "match_score": round(similarity_scores[idx]*100, 2)
        })

    return results

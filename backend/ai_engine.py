from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_assignment(text, previous_texts):
    if not previous_texts:
        return "0%", 85, "Good start"

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text] + previous_texts)

    similarity = cosine_similarity(vectors[0:1], vectors[1:]).max()
    plagiarism = f"{round(similarity * 100, 2)}%"

    score = max(50, int(100 - similarity * 40))
    feedback = "Needs improvement" if score < 75 else "Well done"

    return plagiarism, score, feedback
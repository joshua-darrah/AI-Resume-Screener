from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import consine_similarity

def match_resume_to_job(resume_text, job_description):
    documents = [resume_text, job_description]

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    # Calculate cosine similarities
    similarity = consine_similarity(vectors[0], vectors[1])

    # Convert to percentage
    match_score = round(similarity[0][0] * 100, 2)

    return match_score
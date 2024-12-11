import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

def apply_nlp_techniques(queries):
    vectorizer = CountVectorizer(stop_words='english')
    query_matrix = vectorizer.fit_transform(queries)
    return query_matrix, vectorizer

def perform_topic_modeling(query_matrix, n_topics=5):
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(query_matrix)
    return lda

def display_topics(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

def visualize_topic_distribution(model, query_matrix):
    topic_distribution = model.transform(query_matrix)
    topic_counts = topic_distribution.argmax(axis=1)
    plt.hist(topic_counts, bins=model.n_components, align='left', rwidth=0.8)
    plt.xlabel('Topic')
    plt.ylabel('Number of Queries')
    plt.title('Topic Distribution in Conversations')
    plt.show()

if __name__ == "__main__":
    # Assuming the data has been extracted and organized into a DataFrame
    df = pd.read_csv('extracted_data.csv')
    queries = df['Query'].tolist()

    query_matrix, vectorizer = apply_nlp_techniques(queries)
    lda_model = perform_topic_modeling(query_matrix)

    n_top_words = 10
    display_topics(lda_model, vectorizer.get_feature_names_out(), n_top_words)
    visualize_topic_distribution(lda_model, query_matrix)

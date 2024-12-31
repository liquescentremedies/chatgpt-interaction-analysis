import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

def apply_nlp_techniques(queries):
    vectorizer = CountVectorizer(stop_words='english', min_df=2)
    query_matrix = vectorizer.fit_transform(queries)
    return query_matrix, vectorizer

def perform_topic_modeling(query_matrix, n_topics=5):
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(query_matrix)
    return lda

def get_topic_words(model, feature_names, n_top_words):
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        topics.append({
            'topic_id': topic_idx,
            'words': ', '.join(top_words)
        })
    return pd.DataFrame(topics)

def get_document_topics(model, query_matrix, queries):
    topic_distribution = model.transform(query_matrix)
    dominant_topics = topic_distribution.argmax(axis=1)
    
    return pd.DataFrame({
        'Query': queries,
        'Topic': dominant_topics,
        'TopicProbability': [dist[topic] for dist, topic in zip(topic_distribution, dominant_topics)]
    })

def visualize_topic_distribution(model, query_matrix, filename):
    topic_distribution = model.transform(query_matrix)
    topic_counts = topic_distribution.argmax(axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.hist(topic_counts, bins=model.n_components, align='left', rwidth=0.8)
    plt.xlabel('Topic')
    plt.ylabel('Number of Queries')
    plt.title('Topic Distribution in Conversations')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    try:
        # Load the extracted data
        df = pd.read_csv('extracted_data.csv')
        queries = df['Query'].tolist()

        # Perform topic modeling
        query_matrix, vectorizer = apply_nlp_techniques(queries)
        lda_model = perform_topic_modeling(query_matrix)

        # Get topic words and document-topic assignments
        n_top_words = 10
        topic_words_df = get_topic_words(lda_model, vectorizer.get_feature_names_out(), n_top_words)
        document_topics_df = get_document_topics(lda_model, query_matrix, queries)

        # Save results
        topic_words_df.to_csv('topic_words.csv', index=False)
        document_topics_df.to_csv('topic_modeling.csv', index=False)
        print("Topic modeling results saved to topic_words.csv and topic_modeling.csv")

        # Generate visualization
        visualize_topic_distribution(lda_model, query_matrix, 'topic_distribution.png')
        print("Topic distribution visualization saved as topic_distribution.png")

        # Display topic words
        print("\nTop words in each topic:")
        for _, row in topic_words_df.iterrows():
            print(f"\nTopic {row['topic_id']}:")
            print(row['words'])

    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing topic modeling: {str(e)}")

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def preprocess_data(queries):
    vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
    X = vectorizer.fit_transform(queries)
    return X, vectorizer

def classify_queries_kmeans(X, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X)
    return kmeans, clusters

def get_cluster_keywords(vectorizer, kmeans, n_words=5):
    feature_names = vectorizer.get_feature_names_out()
    clusters_keywords = []
    
    for cluster_center in kmeans.cluster_centers_:
        top_indices = cluster_center.argsort()[::-1][:n_words]
        keywords = [feature_names[i] for i in top_indices]
        clusters_keywords.append(', '.join(keywords))
    
    return clusters_keywords

def visualize_cluster_distribution(clusters, filename):
    plt.figure(figsize=(10, 6))
    plt.hist(clusters, bins=len(np.unique(clusters)), align='left', rwidth=0.8)
    plt.xlabel('Cluster')
    plt.ylabel('Number of Queries')
    plt.title('Query Category Distribution')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    try:
        # Load the extracted data
        df = pd.read_csv('extracted_data.csv')
        queries = df['Query'].tolist()

        # Preprocess and classify queries
        X, vectorizer = preprocess_data(queries)
        kmeans, clusters = classify_queries_kmeans(X)

        # Get cluster keywords
        cluster_keywords = get_cluster_keywords(vectorizer, kmeans)

        # Create results DataFrame
        results_df = pd.DataFrame({
            'Query': queries,
            'Category': clusters,
            'CategoryKeywords': [cluster_keywords[c] for c in clusters]
        })

        # Save results
        results_df.to_csv('query_classification.csv', index=False)
        print("Query classification results saved to query_classification.csv")

        # Generate visualization
        visualize_cluster_distribution(clusters, 'query_categories.png')
        print("Query category distribution visualization saved as query_categories.png")

        # Display cluster information
        print("\nQuery Categories and their Keywords:")
        for i, keywords in enumerate(cluster_keywords):
            print(f"\nCategory {i}:")
            print(f"Keywords: {keywords}")
            print(f"Number of queries: {(clusters == i).sum()}")

    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing query classification: {str(e)}")

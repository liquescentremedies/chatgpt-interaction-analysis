import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def categorize_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def perform_sentiment_analysis(queries, responses):
    query_sentiments = [categorize_sentiment(analyze_sentiment(query)) for query in queries]
    response_sentiments = [categorize_sentiment(analyze_sentiment(response)) for response in responses]
    return query_sentiments, response_sentiments

def visualize_sentiment_distribution(sentiments, title):
    sentiment_counts = pd.Series(sentiments).value_counts()
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title(title)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    # Assuming the data has been extracted and organized into a DataFrame
    df = pd.read_csv('extracted_data.csv')
    queries = df['Query'].tolist()
    responses = df['Response'].tolist()

    query_sentiments, response_sentiments = perform_sentiment_analysis(queries, responses)

    visualize_sentiment_distribution(query_sentiments, 'Query Sentiment Distribution')
    visualize_sentiment_distribution(response_sentiments, 'Response Sentiment Distribution')

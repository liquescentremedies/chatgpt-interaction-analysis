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
    
    # Create DataFrame with results
    sentiment_df = pd.DataFrame({
        'Query': queries,
        'Response': responses,
        'QuerySentiment': query_sentiments,
        'ResponseSentiment': response_sentiments
    })
    return sentiment_df

def visualize_sentiment_distribution(sentiments, title):
    sentiment_counts = pd.Series(sentiments).value_counts()
    plt.figure(figsize=(10, 6))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title(title)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f"{title.lower().replace(' ', '_')}.png")
    plt.close()

if __name__ == "__main__":
    try:
        # Load the extracted data
        df = pd.read_csv('extracted_data.csv')
        queries = df['Query'].tolist()
        responses = df['Response'].tolist()

        # Perform sentiment analysis
        sentiment_df = perform_sentiment_analysis(queries, responses)
        
        # Save results to CSV
        sentiment_df.to_csv('sentiment_analysis.csv', index=False)
        print("Sentiment analysis results saved to sentiment_analysis.csv")

        # Generate visualizations
        visualize_sentiment_distribution(sentiment_df['QuerySentiment'], 'Query Sentiment Distribution')
        visualize_sentiment_distribution(sentiment_df['ResponseSentiment'], 'Response Sentiment Distribution')
        print("Sentiment visualizations saved as PNG files")
        
    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing sentiment analysis: {str(e)}")

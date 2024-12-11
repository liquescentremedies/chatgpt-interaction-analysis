import pandas as pd
import matplotlib.pyplot as plt

def combine_insights():
    # Load data from various analyses
    df_extracted = pd.read_csv('extracted_data.csv')
    df_sentiment = pd.read_csv('sentiment_analysis.csv')
    df_temporal = pd.read_csv('temporal_analysis.csv')
    df_topic = pd.read_csv('topic_modeling.csv')
    df_query_classification = pd.read_csv('query_classification.csv')
    df_response_time = pd.read_csv('response_time_analysis.csv')

    # Combine data into a single DataFrame
    combined_df = df_extracted.copy()
    combined_df['Sentiment'] = df_sentiment['Sentiment']
    combined_df['InteractionCount'] = df_temporal['InteractionCount']
    combined_df['Topic'] = df_topic['Topic']
    combined_df['QueryCategory'] = df_query_classification['Category']
    combined_df['ResponseTime'] = df_response_time['ResponseTime']

    return combined_df

def generate_summary_report(combined_df):
    summary = {
        'Total Queries': combined_df.shape[0],
        'Positive Sentiment': (combined_df['Sentiment'] == 'Positive').sum(),
        'Negative Sentiment': (combined_df['Sentiment'] == 'Negative').sum(),
        'Neutral Sentiment': (combined_df['Sentiment'] == 'Neutral').sum(),
        'Most Frequent Topic': combined_df['Topic'].mode()[0],
        'Most Common Query Category': combined_df['QueryCategory'].mode()[0],
        'Average Response Time': combined_df['ResponseTime'].mean()
    }
    return summary

def visualize_synthesized_insights(combined_df):
    # Sentiment Distribution
    sentiment_counts = combined_df['Sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

    # Interaction Frequency Over Time
    interaction_counts = combined_df['InteractionCount']
    interaction_counts.plot(kind='line')
    plt.title('Interaction Frequency Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Interactions')
    plt.show()

    # Topic Distribution
    topic_counts = combined_df['Topic'].value_counts()
    topic_counts.plot(kind='bar')
    plt.title('Topic Distribution')
    plt.xlabel('Topic')
    plt.ylabel('Count')
    plt.show()

    # Query Category Distribution
    query_category_counts = combined_df['QueryCategory'].value_counts()
    query_category_counts.plot(kind='bar')
    plt.title('Query Category Distribution')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()

    # Response Time Distribution
    response_times = combined_df['ResponseTime']
    plt.hist(response_times, bins=50, edgecolor='k')
    plt.title('Response Time Distribution')
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    combined_df = combine_insights()
    summary_report = generate_summary_report(combined_df)
    print(summary_report)
    visualize_synthesized_insights(combined_df)

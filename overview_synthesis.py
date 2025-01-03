import pandas as pd
import matplotlib.pyplot as plt

def load_analysis_data():
    try:
        data = {
            'extracted': pd.read_csv('extracted_data.csv'),
            'sentiment': pd.read_csv('sentiment_analysis.csv'),
            'temporal': pd.read_csv('temporal_analysis.csv'),
            'topic': pd.read_csv('topic_modeling.csv'),
            'query': pd.read_csv('query_classification.csv'),
            'response_time': pd.read_csv('response_time_analysis.csv'),
            'patterns': pd.read_csv('conversation_patterns.csv')
        }
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing analysis file: {str(e)}")

def combine_insights(data):
    combined_df = data['extracted'].copy()
    
    # Add sentiment analysis results
    combined_df['QuerySentiment'] = data['sentiment']['QuerySentiment']
    combined_df['ResponseSentiment'] = data['sentiment']['ResponseSentiment']
    
    # Add temporal analysis results
    combined_df = combined_df.merge(data['temporal'], on='Timestamp', how='left')
    
    # Add topic modeling results
    combined_df['Topic'] = data['topic']['Topic']
    combined_df['TopicKeywords'] = data['topic']['CategoryKeywords']
    
    # Add query classification results
    combined_df['QueryCategory'] = data['query']['Category']
    combined_df['CategoryKeywords'] = data['query']['CategoryKeywords']
    
    return combined_df

def generate_summary_report(combined_df, word_freq_df):
    summary = {
        'Overview': {
            'Total Interactions': combined_df.shape[0],
            'Unique Topics': combined_df['Topic'].nunique(),
            'Query Categories': combined_df['QueryCategory'].nunique()
        },
        'Sentiment Analysis': {
            'Positive Queries': (combined_df['QuerySentiment'] == 'Positive').sum(),
            'Negative Queries': (combined_df['QuerySentiment'] == 'Negative').sum(),
            'Neutral Queries': (combined_df['QuerySentiment'] == 'Neutral').sum()
        },
        'Response Times': {
            'Average Response Time': f"{combined_df['ResponseTime'].mean():.2f} seconds",
            'Fastest Response': f"{combined_df['ResponseTime'].min():.2f} seconds",
            'Slowest Response': f"{combined_df['ResponseTime'].max():.2f} seconds"
        },
        'Top Themes': word_freq_df.head(10).to_dict('records')
    }
    return summary

def save_visualizations(combined_df):
    # Sentiment Distribution
    plt.figure(figsize=(10, 6))
    combined_df['QuerySentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title('Query Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('overview_sentiment.png')
    plt.close()

    # Topic Distribution
    plt.figure(figsize=(10, 6))
    combined_df['Topic'].value_counts().plot(kind='bar')
    plt.title('Topic Distribution')
    plt.xlabel('Topic')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('overview_topics.png')
    plt.close()

    # Query Category Distribution
    plt.figure(figsize=(10, 6))
    combined_df['QueryCategory'].value_counts().plot(kind='bar')
    plt.title('Query Category Distribution')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('overview_categories.png')
    plt.close()

if __name__ == "__main__":
    try:
        # Load all analysis results
        analysis_data = load_analysis_data()
        
        # Combine insights
        combined_df = combine_insights(analysis_data)
        
        # Generate and save summary report
        summary_report = generate_summary_report(combined_df, analysis_data['patterns'])
        with open('analysis_summary.json', 'w') as f:
            json.dump(summary_report, f, indent=2)
        print("Analysis summary saved to analysis_summary.json")
        
        # Generate and save visualizations
        save_visualizations(combined_df)
        print("Overview visualizations saved as PNG files")
        
        # Display key findings
        print("\nKey Findings:")
        print(f"Total Interactions: {summary_report['Overview']['Total Interactions']}")
        print(f"Most Common Sentiment: {combined_df['QuerySentiment'].mode()[0]}")
        print(f"Average Response Time: {summary_report['Response Times']['Average Response Time']}")
        print("\nTop 5 Themes:")
        for theme in summary_report['Top Themes'][:5]:
            print(f"{theme['word']}: {theme['frequency']} occurrences")
            
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        print("Please ensure all analysis scripts have been run in the correct order:")
        print("1. data_extraction.py")
        print("2. sentiment_analysis.py")
        print("3. temporal_analysis.py")
        print("4. topic_modeling.py")
        print("5. query_classification.py")
        print("6. response_time_analysis.py")
        print("7. conversation_pattern_analysis.py")
    except Exception as e:
        print(f"Error generating overview: {str(e)}")

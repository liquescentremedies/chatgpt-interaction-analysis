import pandas as pd
import matplotlib.pyplot as plt

def analyze_interaction_patterns(timestamps):
    timestamps = pd.to_datetime(timestamps)
    interaction_counts = timestamps.value_counts().sort_index()
    return interaction_counts

def visualize_interaction_frequency(interaction_counts, title, filename):
    plt.figure(figsize=(12, 6))
    interaction_counts.plot(kind='line')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Number of Interactions')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def identify_engagement_trends(interaction_counts):
    rolling_mean = interaction_counts.rolling(window=7).mean()
    return rolling_mean

if __name__ == "__main__":
    try:
        # Load the extracted data
        df = pd.read_csv('extracted_data.csv')
        timestamps = df['Timestamp'].tolist()

        # Analyze interaction patterns
        interaction_counts = analyze_interaction_patterns(timestamps)
        
        # Save temporal analysis results
        temporal_df = pd.DataFrame({
            'Timestamp': interaction_counts.index,
            'InteractionCount': interaction_counts.values
        })
        temporal_df.to_csv('temporal_analysis.csv', index=False)
        print("Temporal analysis results saved to temporal_analysis.csv")

        # Generate and save visualizations
        visualize_interaction_frequency(interaction_counts, 
                                     'Interaction Frequency Over Time',
                                     'interaction_frequency.png')

        engagement_trends = identify_engagement_trends(interaction_counts)
        visualize_interaction_frequency(engagement_trends, 
                                     'Engagement Trends (7-day Moving Average)',
                                     'engagement_trends.png')
        print("Temporal analysis visualizations saved as PNG files")

    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing temporal analysis: {str(e)}")

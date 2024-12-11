import pandas as pd
import matplotlib.pyplot as plt

def analyze_interaction_patterns(timestamps):
    timestamps = pd.to_datetime(timestamps)
    interaction_counts = timestamps.value_counts().sort_index()
    return interaction_counts

def visualize_interaction_frequency(interaction_counts):
    plt.figure(figsize=(12, 6))
    interaction_counts.plot(kind='line')
    plt.title('Interaction Frequency Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Interactions')
    plt.show()

def identify_engagement_trends(interaction_counts):
    rolling_mean = interaction_counts.rolling(window=7).mean()
    return rolling_mean

if __name__ == "__main__":
    # Assuming the data has been extracted and organized into a DataFrame
    df = pd.read_csv('extracted_data.csv')
    timestamps = df['Timestamp'].tolist()

    interaction_counts = analyze_interaction_patterns(timestamps)
    visualize_interaction_frequency(interaction_counts)

    engagement_trends = identify_engagement_trends(interaction_counts)
    visualize_interaction_frequency(engagement_trends)

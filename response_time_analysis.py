import pandas as pd
import matplotlib.pyplot as plt

def evaluate_response_promptness(timestamps, response_times):
    response_data = pd.DataFrame({
        'Timestamp': pd.to_datetime(timestamps),
        'ResponseTime': response_times
    })
    return response_data

def analyze_response_times(response_data):
    response_time_stats = {
        'mean': response_data['ResponseTime'].mean(),
        'median': response_data['ResponseTime'].median(),
        'std': response_data['ResponseTime'].std(),
        'min': response_data['ResponseTime'].min(),
        'max': response_data['ResponseTime'].max()
    }
    return response_time_stats

def visualize_response_time_distribution(response_data, filename):
    plt.figure(figsize=(12, 6))
    plt.hist(response_data['ResponseTime'], bins=50, edgecolor='k')
    plt.title('Response Time Distribution')
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    try:
        # Load the extracted data
        df = pd.read_csv('extracted_data.csv')
        timestamps = df['Timestamp'].tolist()
        response_times = df['ResponseTime'].tolist()

        # Analyze response times
        response_data = evaluate_response_promptness(timestamps, response_times)
        response_time_stats = analyze_response_times(response_data)

        # Save results
        response_data.to_csv('response_time_analysis.csv', index=False)
        print("Response time analysis results saved to response_time_analysis.csv")

        # Generate visualization
        visualize_response_time_distribution(response_data, 'response_time_distribution.png')
        print("Response time distribution visualization saved as response_time_distribution.png")

        # Display statistics
        print("\nResponse Time Statistics:")
        for stat, value in response_time_stats.items():
            print(f"{stat.capitalize()}: {value:.2f} seconds")

    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing response time analysis: {str(e)}")

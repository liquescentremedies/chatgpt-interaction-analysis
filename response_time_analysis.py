import pandas as pd
import matplotlib.pyplot as plt

def evaluate_response_promptness(timestamps, response_times):
    """
    Evaluate the promptness of responses by creating a DataFrame with timestamps and response times.

    Args:
        timestamps (list): List of timestamps.
        response_times (list): List of response times.

    Returns:
        DataFrame: A DataFrame with timestamps and response times.
    """
    resp_data = pd.DataFrame({
        'Timestamp': pd.to_datetime(timestamps),
        'ResponseTime': response_times
    })
    return resp_data

def analyze_response_times(resp_data):
    """
    Analyze response times to calculate statistical measures.

    Args:
        resp_data (DataFrame): DataFrame with response times.

    Returns:
        dict: A dictionary with statistical measures of response times.
    """
    resp_time_stats = {
        'mean': resp_data['ResponseTime'].mean(),
        'median': resp_data['ResponseTime'].median(),
        'std': resp_data['ResponseTime'].std(),
        'min': resp_data['ResponseTime'].min(),
        'max': resp_data['ResponseTime'].max()
    }
    return resp_time_stats

def visualize_response_time_distribution(resp_data, filename):
    """
    Visualize the distribution of response times and save the plot to a file.

    Args:
        resp_data (DataFrame): DataFrame with response times.
        filename (str): The filename to save the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.hist(resp_data['ResponseTime'], bins=50, edgecolor='k')
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
        resp_data = evaluate_response_promptness(timestamps, response_times)
        resp_time_stats = analyze_response_times(resp_data)

        # Save results
        resp_data.to_csv('response_time_analysis.csv', index=False)
        print("Response time analysis results saved to response_time_analysis.csv")

        # Generate visualization
        visualize_response_time_distribution(resp_data, 'response_time_distribution.png')
        print("Response time distribution visualization saved as response_time_distribution.png")

        # Display statistics
        print("\nResponse Time Statistics:")
        for stat, value in resp_time_stats.items():
            print(f"{stat.capitalize()}: {value:.2f} seconds")

    except FileNotFoundError:
        print("Error: extracted_data.csv not found. Please run data_extraction.py first.")
    except Exception as e:
        print(f"Error performing response time analysis: {str(e)}")

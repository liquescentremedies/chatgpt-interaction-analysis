import pandas as pd
import matplotlib.pyplot as plt

def evaluate_response_promptness(timestamps, response_times):
    response_data = pd.DataFrame({
        'Timestamp': pd.to_datetime(timestamps),
        'ResponseTime': response_times
    })
    return response_data

def analyze_response_times(response_data):
    response_data['ResponseTime'] = pd.to_timedelta(response_data['ResponseTime'])
    response_time_stats = response_data['ResponseTime'].describe()
    return response_time_stats

def visualize_response_time_distribution(response_data):
    plt.figure(figsize=(12, 6))
    plt.hist(response_data['ResponseTime'].dt.total_seconds(), bins=50, edgecolor='k')
    plt.title('Response Time Distribution')
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    # Assuming the data has been extracted and organized into a DataFrame
    df = pd.read_csv('extracted_data.csv')
    timestamps = df['Timestamp'].tolist()
    response_times = df['ResponseTime'].tolist()

    response_data = evaluate_response_promptness(timestamps, response_times)
    response_time_stats = analyze_response_times(response_data)
    print(response_time_stats)

    visualize_response_time_distribution(response_data)

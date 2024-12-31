import json
import pandas as pd

def upload_and_read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_essential_data(data):
    queries = []
    responses = []
    timestamps = []
    response_times = []
    last_query_time = None

    for conversation in data['conversations']:
        for message in conversation['messages']:
            if message['role'] == 'user':
                queries.append(message['content'])
                timestamps.append(message['timestamp'])
                last_query_time = message['timestamp']
            elif message['role'] == 'assistant':
                responses.append(message['content'])
                if last_query_time:
                    response_time = (message['timestamp'] - last_query_time).total_seconds()
                    response_times.append(response_time)
                else:
                    response_times.append(None)

    return queries, responses, timestamps, response_times

def organize_data(queries, responses, timestamps, response_times):
    data_dict = {
        'Query': queries,
        'Response': responses,
        'Timestamp': timestamps,
        'ResponseTime': response_times
    }
    df = pd.DataFrame(data_dict)
    return df

if __name__ == "__main__":
    try:
        file_path = 'model_comparisons.json'
        data = upload_and_read_json(file_path)
        queries, responses, timestamps, response_times = extract_essential_data(data)
        df = organize_data(queries, responses, timestamps, response_times)
        
        # Save to CSV for other analysis scripts
        df.to_csv('extracted_data.csv', index=False)
        print("Data extracted and saved to extracted_data.csv")
        print("\nFirst few rows:")
        print(df.head())
    except FileNotFoundError:
        print("Error: model_comparisons.json file not found. Please ensure the file exists in the current directory.")
    except Exception as e:
        print(f"Error processing data: {str(e)}")

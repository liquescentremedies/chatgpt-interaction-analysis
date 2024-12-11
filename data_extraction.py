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

    for conversation in data['conversations']:
        for message in conversation['messages']:
            if message['role'] == 'user':
                queries.append(message['content'])
                timestamps.append(message['timestamp'])
            elif message['role'] == 'assistant':
                responses.append(message['content'])

    return queries, responses, timestamps

def organize_data(queries, responses, timestamps):
    data_dict = {
        'Query': queries,
        'Response': responses,
        'Timestamp': timestamps
    }
    df = pd.DataFrame(data_dict)
    return df

if __name__ == "__main__":
    file_path = 'model_comparisons.json'
    data = upload_and_read_json(file_path)
    queries, responses, timestamps = extract_essential_data(data)
    df = organize_data(queries, responses, timestamps)
    print(df.head())

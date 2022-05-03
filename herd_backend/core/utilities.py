import json

def process_for_response(raw_data, metadata=None):
    dict_data = json.loads(raw_data)
    processed = {column: list(dict_data[column].values()) for column in dict_data}
    if metadata:
        processed['metadata'] = metadata
    return processed

def get_columns(raw_data: str):
    return list(json.loads(raw_data).keys())

def convert_to_json(raw: str):
    return json.loads(raw)
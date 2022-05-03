import json
from django.http import JsonResponse


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

def makeJsonResponse(response_body, metadata=None, is_modified=False):
    if is_modified:
        return JsonResponse(process_for_response(response_body, metadata), safe=False)

    return JsonResponse(convert_to_json(response_body), safe=False)
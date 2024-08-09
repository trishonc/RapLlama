import requests
from dotenv import load_dotenv
import os
load_dotenv()

def extract_text(node):
    """
    Recursively extract and concatenate text from a nested structure.
    """
    if isinstance(node, str):
        return node
    elif isinstance(node, dict):
        if 'children' in node:
            return ''.join(extract_text(child) for child in node['children'])
    elif isinstance(node, list):
        return ''.join(extract_text(item) for item in node)
    return ''

token = os.getenv('CLIENT_ACCESS_TOKEN')

def get_annotations() -> dict:
    headers = {'Authorization': f'Bearer {token}'}
    dict = {}
    annotations = []
    referents = []
    url = 'https://api.genius.com/referents'
    params = {'song_id': '235729', 'per_page': '50'}
    response = requests.get(url, params=params, headers=headers)
    json_response = response.json()
    items = json_response['response']['referents']

    for item in items:
        referents.append(item['fragment'])
        annotations.append(extract_text(item['annotations'][0]['body']['dom']))

    for referent, annotation in zip(referents, annotations):
        dict[referent] = annotation
    return dict


dict = get_annotations()

print(len(dict))
for k, v in dict.items():
    print(f'{k}:\n{v}')
    print()
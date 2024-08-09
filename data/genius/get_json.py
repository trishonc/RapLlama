import requests

def safe_get_json(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  
        return response.json() 
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"Error decoding JSON: {json_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None 

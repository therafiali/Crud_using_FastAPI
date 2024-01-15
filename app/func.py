import requests
import json


BASE_URL = "http://127.0.0.1:8000"

# Function to get all todos from the API
def get_all_todos():
    """Get List of all Todos"""
    response = requests.get(f"{BASE_URL}/")  # Send GET request to API
    res_json = response.json()  # Convert response to JSON
    res_str = json.dumps(res_json)  # Convert JSON to string
    return res_str  # Return string

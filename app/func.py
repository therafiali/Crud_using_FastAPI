import requests
import json

from app.streamlit_client import BASE_URL

BASE_URL

# Function to get all todos from the API
def get_all_todos():
    """Get List of all Todos"""
    response = requests.get(f"{BASE_URL}/")  # Send GET request to API
    res_json = response.json()  # Convert response to JSON
    res_str = json.dumps(res_json)  # Convert JSON to string
    return res_str  # Return string

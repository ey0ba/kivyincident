import requests
from config import API_URLS, HEADERS

def login(username, password):
    """Authenticate user using username and password."""
    url = API_URLS["kivy-login"]
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, json=data, headers=HEADERS)
        if response.status_code == 200:
            return True, response.json()
        return False, "Invalid credentials"
    except requests.RequestException as e:
        return False, f"Network error: {e}"

def fetch_dropdown_data(username, password):
    """Fetch dropdown data from the API."""
    url = API_URLS["dropdown_data"]
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, json=data, headers=HEADERS)
        if response.status_code == 200:
            return True, response.json()
        return False, response.json().get("detail", "Failed to fetch dropdown data.")
    except requests.RequestException as e:
        return False, f"Network error: {e}"




def submit_incident(data, username, password):
    """Submit an incident report with authentication."""
    url = API_URLS["submit_incident"]
    auth_data = {"username": username, "password": password}
    payload = {**auth_data, **data}  # Combine authentication and incident data
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        if response.status_code == 201:
            return True, "Incident submitted successfully!"
        return False, response.json().get("detail", "Submission failed.")
    except requests.RequestException as e:
        return False, f"Network error: {e}"

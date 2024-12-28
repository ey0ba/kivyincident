#BASE_URL = "https://incident.com.et/api/"

#BASE_URL = "http://127.0.0.1:8000/api/kivyapp/"

BASE_URL = "https://incident.com.et/api/kivyapp/"

API_URLS = {
    "kivy-login": f"{BASE_URL}kivy-login/",  # Updated for username-password login
    "dropdown_data": f"{BASE_URL}dropdown-data/",
    "submit_incident": f"{BASE_URL}submit-incident/",
}

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Kivy-App",
}

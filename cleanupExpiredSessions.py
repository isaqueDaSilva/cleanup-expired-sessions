import requests
import os
import schedule
import time
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv('API_URL', 'https://api.example.com/cleanup-sessions')
API_KEY = os.getenv('API_KEY', 'your_default_api_key')
HEADERS = {'Authorization': f'Bearer {API_KEY}'}

def cleanup_expired_sessions():
    try:
        print("Starting cleanup of expired sessions...")
        response = requests.delete(API_URL, headers=HEADERS)
        response.raise_for_status()
        response_data = response.json()
        print(f"Expired sessions cleaned up successfully. Response: {response_data}")
    except requests.exceptions.RequestException as e:
        print(f"Error during cleanup: {e}")

# Schedule the cleanup to run daily at midnight
schedule.every().day.at("00:00").do(cleanup_expired_sessions)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute between checks
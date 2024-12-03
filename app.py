import time
import requests

# Replace with your Flask app's Render URL
URL = "https://rsse-flask.onrender.com/"

# Interval in seconds (e.g., every 14 minutes = 840 seconds)
INTERVAL = 840  

def keep_alive():
    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                print(f"Ping successful: {response.status_code}")
            else:
                print(f"Ping failed: {response.status_code}")
        except Exception as e:
            print(f"Error pinging the URL: {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    keep_alive()

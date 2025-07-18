import requests
import os # <-- 1. Import the 'os' module

# -- 2. Add this line before making the request --
# This tells requests (and other libraries) to NOT use a proxy for these addresses.
os.environ['NO_PROXY'] = 'localhost,127.0.0.1' 

# The URL of the server we just started in Jupyter
url = "http://localhost:8000"

print(f"Attempting to connect to {url}...")

try:
    # Send a GET request to the server
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the text content of the response
        print("Successfully connected to the server.")
        print(f"Response from server: '{response.text}'")
    else:
        print(f"Error: Server returned status code {response.status_code}")

except requests.exceptions.ProxyError as e:
    print(f"\nCaught a Proxy Error. This confirms a proxy issue.")
    print(f"The 'NO_PROXY' setting should fix this. Error details: {e}")

except requests.exceptions.ConnectionError as e:
    print(f"\nConnection failed: Could not connect to the server at {url}.")
    print("Please ensure the Jupyter server code is running and not blocked by a firewall.")
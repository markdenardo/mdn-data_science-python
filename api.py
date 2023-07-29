import requests

def call_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"API returned an error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# Replace 'your_api_url_here' with the actual API endpoint URL
api_url = 'your_api_url_here'
result = call_api(api_url)

if result:
    print("API response:")
    print(result)

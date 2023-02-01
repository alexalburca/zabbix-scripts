import requests

def check_url_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up")
        else:
            print(f"{url} is down")
    except requests.exceptions.RequestException as e:
        print(f"{url} is down: {e}")

url = "https://www.google.com" # replace with your URL
check_url_status(url)

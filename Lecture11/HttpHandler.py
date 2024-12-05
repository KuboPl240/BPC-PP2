import requests

class HttpRequestHandler:

    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.ConnectionError:
            return "Connection error occurred."
        except requests.exceptions.Timeout:
            return "Request timed out."
        except requests.exceptions.RequestException as err:
            return f"An error occurred: {err}"

    @staticmethod
    def post(url, data):
        try:
            response = requests.post(url, json=data)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.ConnectionError:
            return "Connection error occurred."
        except requests.exceptions.Timeout:
            return "Request timed out."
        except requests.exceptions.RequestException as err:
            return f"An error occurred: {err}"
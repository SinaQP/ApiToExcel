import requests

class Fetch:
    def __init__(self, url):
        self.url = url
        self.headers = {}
        self.response = None

    def get(self):
        """send get method to url"""
        self.response = requests.get(self.url, headers=self.headers)
        return self.response

    def update_url(self, url):
        self.url = url

    def set_token(self, token):
        """set Bearer token to headers"""
        self.headers["Authorization"] = f"Bearer {token}"

    @staticmethod
    def check_response_status_code(response):
        try:
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as error:
            print(f"RequestException: {error}")
            return False

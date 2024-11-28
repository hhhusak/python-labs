class Repository:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_posts(self):
        return self.api_client.get_data("/posts")

    def get_comments(self):
        return self.api_client.get_data("/comments")
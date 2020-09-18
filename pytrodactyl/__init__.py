import requests

class Server:
    def __init__(self, url:str, text:bool=True, plain:bool=False):
        self.url = url
        self.text = text
        self.plain = plain


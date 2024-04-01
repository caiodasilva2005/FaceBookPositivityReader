class User:
    def __init__(self, id, name, token):
        self.id = id
        self.name = name
        self.token = token
        self.pages = []

class Page:
    def __init__(self, id, name, token):
        self.id = id
        self.name = name
        self.token = token
        self.posts = []

class Post:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.reactions = {}
        self.comments = []

class Comment:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.reactions = {}


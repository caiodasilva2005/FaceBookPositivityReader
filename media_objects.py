class User:
    def __init__(self, id, pages):
        self.id = id
        self.pages = pages

class Page:
    def __init__(self, id):
        self.id = id
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


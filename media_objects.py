class User:
    def __init__(self, id, pages):
        self.id = id
        self.pages = pages

class Page:
    def __init__(self, id, user):
        self.id = id
        self.user = user
        self.posts = []

class Post:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.reactions = {}
        self.comments = []

class Comments:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.reactions = {}


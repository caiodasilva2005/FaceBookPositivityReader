# represents Facebook User
class User:
    def __init__(self, id, name, token):
        self.id = id
        self.name = name
        self.token = token
        self.pages = []

# represents Facebook Page
class Page:
    def __init__(self, id, name, token):
        self.id = id
        self.name = name
        self.token = token
        self.photo_path = ""
        self.posts = []

# represents post on page
class Post:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.reactions = {}
        self.comments = []

# represents comment on post
class Comment:
    def __init__(self, id, message):
        self.id = id
        self.message = message
        self.reactions = {}


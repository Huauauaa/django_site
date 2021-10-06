from django.db import models
from datetime import datetime


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


if __name__ == '__main__':
    comment = Comment(email='harvey0379@163.com', content='Hello World')

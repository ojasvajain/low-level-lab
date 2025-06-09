

class Document:
    def __init__(self, _id, content):
        self.content = content
        self.id = _id

    def __str__(self):
        return f'ID - {self.id}, Content - {self.content}'




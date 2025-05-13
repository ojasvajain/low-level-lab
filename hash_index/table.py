from config import CONFIG

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.hash_indexes = dict()
        self.segments = []
        self.config = CONFIG['table']

    def create_hash_index(self, column):
        return

    def insert(self):
        return

    def update(self):
        return

    def delete(self):
        return

    def get(self, key, value):
        return



from hash_index.table import Table

class Database:

    def __init__(self):
        self.tables = dict()

    def create_table(self, table_name, columns):
        if table_name in self.tables:
            raise Exception(f'Table {table_name} already exists in the db')
        self.tables[table_name] = Table(table_name, columns)




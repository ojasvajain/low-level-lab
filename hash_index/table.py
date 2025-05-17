from config import CONFIG
from hash_index.segment_collection import SegmentCollection


class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.hash_indexes = dict()
        self.segments = SegmentCollection(self.name)
        #self.config = CONFIG['table']

    def create_hash_index(self, column):
        hash_index = dict()  # key = column value, value = list of records
        # read all existing data from segments and build index on given column
        print(f'Building Hash index on column - {column}')
        for row in self.segments.iterate_over_all_rows():
            s_id, index, record = row
            if column not in record:
                print(f'[WARNING] Column key not found in record - {record}. Skipping...')
                continue
            key = record[column]
            hash_index[key].append((s_id, index))
        self.hash_indexes[column] = hash_index
        print(f'Hash index created on column - {column}')

    def insert(self, record):
        print(f'Writing Record to Disk')
        _id, index = self.segments.write_to_disk(record)
        for column in self.hash_indexes:
            print(f'Updating Hash Index on {column}')
            hash_index = self.hash_indexes[column]
            key = record[column]
            hash_index[key].append((_id, index))

    def update(self):
        return

    def delete(self):
        return

    def get(self, key, value):
        return
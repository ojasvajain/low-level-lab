import json

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
        for s_id, offset, record in self.segments.iterate_over_all_rows():
            if column not in record:
                print(f'[WARNING] Column key not found in record - {record}. Skipping...')
                continue
            key = record[column]
            if key not in hash_index:
                hash_index[key] = [(s_id, offset)]
            else:
                hash_index[key].append((s_id, offset))
        self.hash_indexes[column] = hash_index
        print(f'Hash index created on column - {column}')
        self.print_hash_table(column)

    def print_hash_table(self, key):
        print(json.dumps(self.hash_indexes[key], indent=1))

    def insert(self, record):
        print(f'Writing Record to Disk')
        _id, offset = self.segments.write_to_disk(record)
        for column in self.hash_indexes:
            print(f'Updating Hash Index on {column}')
            hash_index = self.hash_indexes[column]
            key = record[column]
            if key not in hash_index:
                hash_index[key] = [(_id, offset)]
            else:
                hash_index[key].append((_id, offset))

    # UPDATE <table_name> SET = <updated_value> WHERE <input_key> = <input_value>
    def update(self, input_key, input_value, key_to_update, updated_value):
        records = self.get(input_key, input_value)

        # get (s_id, offsets) of records found
        positions = self.hash_indexes[input_key][input_value].copy()
        # write updated records
        # update hash indexes
        for i in range(len(records)):
            record = records[i]
            updated_record = record.copy()
            updated_record[key_to_update] = updated_value
            _id, offset = self.segments.write_to_disk(updated_record)
            print(f'Update record written for record {i}')

            # only one index needs to be modified
            hash_index = self.hash_indexes[key_to_update]
            value = record[key_to_update]
            hash_index[value].remove(positions[i])
            if updated_value not in hash_index:
                hash_index[updated_value] = [(_id, offset)]
            else:
                hash_index[updated_value].append((_id, offset))
            print(f'Indexes updated for record {i}')

    # DELETE FROM <table_name> WHERE <input_key> = <input_value>
    def delete(self, input_key, input_value):
        # get existing records
        records = self.get(input_key, input_value)
        print(f'{len(records)} records found. Deleting...')

        positions = self.hash_indexes[input_key][input_value].copy()
        # write tombstone records
        # update hash indexes
        for i in range(len(records)):
            record = records[i]
            self.segments.write_to_disk(record, True)
            print(f'Tombstone record written for record {i}')

            for key in self.hash_indexes:
                hash_index = self.hash_indexes[key]
                value = record[key]
                hash_index[value].remove(positions[i])
            print(f'Indexes updated for record {i}')

    # SELECT * FROM <table_name> WHERE <key> = <value>
    def get(self, key, value):
        if key not in self.hash_indexes:
            raise Exception(f'Index not found on {key}')

        if value not in self.hash_indexes[key]:
            raise Exception(f'{value} not found in Index on {key}')

        matched_records = []
        for s_id, offset in self.hash_indexes[key][value]:
            record = self.segments.read_record(s_id, offset)
            matched_records.append(record)
        return matched_records

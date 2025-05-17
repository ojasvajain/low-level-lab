from hash_index.config import CONFIG
import json
import os

class Segment:
    def __init__(self, dir_path, _id):
        self.id = _id
        self.path = f'{dir_path}/segment_{_id}'
        self.config = CONFIG['segment']
        self.num_rows = 0

        if os.path.exists(self.path):
            raise Exception(f'Segment {self.path} already exists')
        open(self.path, 'w').close()

    def iterate_over_rows(self):
        # return row index and id
        index = 0
        with open(self.path, 'r') as f:
            line = f.readline()
            while not line:
                yield index, json.loads(line)
                index += 1
                line = f.readline()

    def append_record(self, row, is_delete = False):
        if self.is_full():
            raise Exception(f'Unable to write to Segment {self.path} as it is full')
        print(f'Writing Record to Segment - {self.id}')
        if is_delete:
            row['_deleted'] = True
        with open(self.path, 'a') as f:
            f.write(json.dumps(row))

        curr_index = self.num_rows
        self.num_rows += 1
        return curr_index

    def is_full(self):
        return self.num_rows >= self.config['max_rows']




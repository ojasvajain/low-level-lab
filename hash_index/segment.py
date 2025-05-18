from hash_index.config import CONFIG
import json
import os


class Segment:
    def __init__(self, dir_path, _id):
        self.id = _id
        self.path = f'{dir_path}/segment_{_id}'
        self.config = CONFIG['segment']
        self.num_records = 0

        if os.path.exists(self.path):
            print(f'Segment {self.path} already exists')
        else:
            open(self.path, 'w').close()

    def iterate_over_records(self):
        with open(self.path, 'rb') as f:
            offset = f.tell()
            while offset != os.path.getsize(self.path):
                yield offset, self.read_record_from_current_pos(f)
                offset = f.tell()

    # format of each record: <size of JSON string$<actual string>
    # example: 24${"xyz":"abc"}\n
    def append_record(self, record, is_delete=False):
        if self.is_full():
            raise Exception(f'Unable to write to Segment {self.path} as it is full')

        rcopy = record.copy()
        print(f'Writing Record to Segment - {self.id}')
        if is_delete:
            rcopy['_deleted'] = True

        offset = os.path.getsize(self.path)
        record_num_bytes = len(json.dumps(rcopy).encode('utf-8'))
        with open(self.path, 'ab') as f:
            f.write(f'{record_num_bytes}${json.dumps(rcopy)}'.encode('utf-8'))
        self.num_records += 1
        return offset

    def is_full(self):
        return self.num_records >= self.config['max_rows']

    def read_record_at_offset(self, offset):
        with open(self.path, 'rb') as f:
            f.seek(offset)
            # read the size of JSON record and convert it into integer
            return self.read_record_from_current_pos(f)

    # Assumes file pointer is already at the beginning of a record
    # After reading, it moves the file pointer to the beginning of the next record
    def read_record_from_current_pos(self, f):
        bytes = ''
        byte = f.read(1)
        if not byte:
            raise Exception(f'Invalid offset for Segment {self.id}')
        while byte != '$'.encode('utf-8'):
            bytes += byte.decode('utf-8')
            byte = f.read(1)

        json_size_in_bytes = int(bytes)

        # now, read the specific no. of bytes
        bytes = f.read(json_size_in_bytes)
        return json.loads(bytes.decode('utf-8'))


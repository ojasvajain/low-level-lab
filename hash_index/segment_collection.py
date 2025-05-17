import os
from hash_index.segment import Segment


class SegmentCollection:

    def __init__(self, table_name):
        self.table_name = table_name
        self.dir_path = f'segments/{table_name}'
        # crete folder for storing segment files
        try:
            os.mkdir(self.dir_path)
        except FileExistsError:
            raise Exception(f'Segment folder {self.dir_path} already exists')
        self.segments = []

    # inserts the record in the current segment or creates one if required
    def write_to_disk(self, record):
        # new segment needs to be created if no segments exist or current segment is full
        if len(self.segments) == 0 or self.segments[-1].is_full():
            self.create_segment()

        curr_segment = self.segments[-1]
        return curr_segment.id, curr_segment.append_record(record)

    def create_segment(self):
        _id = len(self.segments)
        print(f'Creating New Segment - {_id}')
        self.segments.append(Segment(self.dir_path, _id))

    def iterate_over_all_rows(self):
        for s in self.segments:
            for row in s.iterate_over_rows():
                yield s.id, row
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
            print(f'Segment folder {self.dir_path} already exists')

        # todo: add logic to read existing segments
        self.segments = []

    # inserts the record in the current segment or creates one if required
    def write_to_disk(self, record, is_delete=False):
        # new segment needs to be created if no segments exist or current segment is full
        if len(self.segments) == 0 or self.segments[-1].is_full():
            self.create_segment()

        curr_segment = self.segments[-1]
        return curr_segment.id, curr_segment.append_record(record, is_delete)

    def create_segment(self):
        _id = len(self.segments)
        print(f'Creating New Segment - {_id}')
        self.segments.append(Segment(self.dir_path, _id))

    def iterate_over_all_rows(self):
        for s in self.segments:
            for offset, record in s.iterate_over_records():
                yield s.id, offset, record

    def read_record(self, s_id, offset):
        # todo: can use dictionary for storing segments by ids
        segment = None
        for s in self.segments:
            if s.id == s_id:
                segment = s
                break

        if segment is None:
            raise Exception(f'Segment with ID {s_id} not found')

        return segment.read_record_at_offset(offset)
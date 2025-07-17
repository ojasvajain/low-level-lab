import threading
from time import sleep


class KVStore:
    def __init__(self):
        self.dict = dict()
        self.lock = threading.Lock()

    def add(self, key, value):
        self.__validate_key(key)
        self.__validate_value(value)
        with self.lock:
            if key in self.dict:
                raise Exception(f'{key} key already exists')
            self.dict[key] = value

    def get(self, key):
        self.__validate_key(key)
        with self.lock:
            if key not in self.dict:
                raise Exception(f'{key} key does not exist')
            sleep(0.0001)  # to trigger context switch
            return self.dict[key]

    def update(self, key, new_value):
        self.__validate_key(key)
        self.__validate_value(new_value)
        with self.lock:
            if key not in self.dict:
                raise Exception(f'{key} key does not exist')
            self.dict[key] = new_value

    def remove(self, key):
        self.__validate_key(key)
        with self.lock:
            if key not in self.dict:
                raise Exception(f'{key} key does not exist')
            sleep(0.0001)  # to trigger context switch
            del self.dict[key]

    @staticmethod
    def __validate_key(key):
        if type(key) is not str:
            raise Exception('key should be of type string')

    @staticmethod
    def __validate_value(value):
        if type(value) is not str:
            raise Exception('value should be of type string')

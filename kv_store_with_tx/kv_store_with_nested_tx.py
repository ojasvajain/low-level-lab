

class KVStore:
    def __init__(self):
        self.dict_list = [dict()]

    def begin(self):
        curr_dict = self.dict_list[-1]
        self.dict_list.append(curr_dict.copy())

    def rollback(self):
        # Discard current dictionary
        if len(self.dict_list) <= 1:
            print('No transaction to rollback')
            return
        del self.dict_list[-1]

    def commit(self):
        # Copy contents of this dict to the prev dict
        if len(self.dict_list) <= 1:
            print('No transaction to commit')
            return
        self.dict_list[-2] = self.dict_list[-1].copy()
        del self.dict_list[-1]

    def create(self, k, v):
        d = self.__get_dict()
        d[k] = v
        return v

    def read(self, k):
        d = self.__get_dict()
        if k not in d:
            print('Key not found')
            return
        return d[k]

    def update(self, k, v):
        d = self.__get_dict()
        if k not in d:
            print('Key not found')
            return
        d[k] = v
        return v

    def delete(self, k):
        d = self.__get_dict()
        if k not in d:
            print('Key not found')
            return
        del d[k]

    def __get_dict(self):
        return self.dict_list[-1]

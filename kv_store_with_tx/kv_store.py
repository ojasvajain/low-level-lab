

class KVStore:
    def __init__(self):
        self.dict = dict()
        self.in_tx = False
        self.tx_dict = None
        self.tx_changes_list = None

    def begin(self):
        self.in_tx = True
        self.tx_dict = self.dict.copy()
        self.tx_changes_list = []

    def rollback(self, n=None):
        if n is None:
            self.tx_dict = None
            self.tx_changes_list = None
            self.in_tx = False
        else:
            self.commit(max(len(self.tx_changes_list) - n, 0))

    def commit(self, n=None):
        if n is None:
            # commit everything
            self.dict = self.tx_dict.copy()
        else:
            # commit first n operations
            for i in range(min(n, len(self.tx_changes_list))):
                change_key, change_val = self.tx_changes_list[i]
                if change_val is None:
                    # tombstone record
                    del self.dict[change_key]
                else:
                    self.dict[change_key] = change_val

        self.tx_dict = None
        self.tx_changes_list = None
        self.in_tx = False

    def create(self, k, v):
        return self.__update_value_of_key(k, v)

    def read(self, k):
        d = self.__get_dict()
        if k not in d:
            #print(f'{k} key not found in dict')
            return None
        return d[k]

    def update(self, k, v):
        if k not in self.__get_dict():
            #print(f'{k} key not found in dict')
            return None
        return self.__update_value_of_key(k, v)

    def delete(self, k):
        d = self.__get_dict()
        if k not in d:
            #print(f'{k} key not found in dict')
            return None
        self.__update_value_of_key(k, None)

    def __get_dict(self):
        if self.in_tx:
            return self.tx_dict
        return self.dict

    def __update_value_of_key(self, k, v):
        if self.in_tx:
            self.tx_changes_list.append((k, v))
            self.tx_dict[k] = v
        else:
            self.dict[k] = v
        return v

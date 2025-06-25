from kv_store import KVStore


def driver():
    kv_store = KVStore()
    kv_store.add('1', '2')
    print(kv_store.get('1'))
    kv_store.update('1', '3')
    print(kv_store.get('1'))
    kv_store.remove('1')
    print(kv_store.get('1'))


if __name__ == '__main__':
    driver()
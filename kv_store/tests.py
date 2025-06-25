import unittest
from kv_store import KVStore
from threading import Thread
import time


class TestKVStoreSingleThreaded(unittest.TestCase):
    kv_store = None

    def setUp(self):
        self.kv_store = KVStore()

    def test_kv_store_validation(self):
        with self.assertRaises(Exception):
            self.kv_store.add(1, '2')

        try:
            self.kv_store.add('1', '2')
        except Exception:
            self.fail('Exception was thrown')

    def test_kv_store_single_threaded(self):
        self.kv_store.add('1', '2')
        self.assertEqual('2', self.kv_store.get('1'))

        self.kv_store.update('1', '3')
        self.assertEqual('3', self.kv_store.get('1'))

        self.kv_store.remove('1')
        with self.assertRaises(Exception):
            self.kv_store.get('1')

    def test_kv_store_multi_threaded(self):
        error = None

        def work_remove():
            nonlocal error
            try:
                self.kv_store.remove('1')
            except:
                error = 'exception not expected while removing'

        def work_get():
            nonlocal error
            try:
                self.kv_store.get('1')
            except KeyError:
                error = 'key error exception occurred'
            except Exception:
                pass

        for i in range(5):
            self.setUp()
            self.kv_store.add('1', '2')
            threads = [
                Thread(target=work_remove),
                Thread(target=work_get),
                Thread(target=work_get),
                Thread(target=work_get),
                Thread(target=work_get)
            ]

            for t in threads:
                t.start()

            for t in threads:
                t.join()

            self.assertIsNone(error)


if __name__ == '__main__':
    unittest.main()

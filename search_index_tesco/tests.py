from search_index import SearchIndex
from document import Document
import unittest


class TestSearchIndex(unittest.TestCase):
    def test_string_1(self):
        search_index = SearchIndex()

        d1 = Document(1, 'Amul Milk')
        d2 = Document(1, 'Amul Milk')
        d3 = Document(2, 'Nandini Chocolate Milk')
        d4 = Document(3, 'Milk Chocolate')
        d5 = Document(4, 'Chocolate Milk')
        d6 = Document(5, 'Milky Way Chocolate Bar')
        search_index.add_doc(d1)
        search_index.add_doc(d2)
        search_index.add_doc(d3)
        search_index.add_doc(d4)
        search_index.add_doc(d5)
        search_index.add_doc(d6)

        expected_result_1 = [
            (d4, 100), (d5, 100), (d3, 63)
        ]
        expected_result_2 = [
            (d5, 100), (d4, 100), (d3, 63)
        ]

        actual_result = search_index.get_search_results('Chocolate Milk')
        self.assertTrue(actual_result == expected_result_1 or actual_result == expected_result_2)


if __name__ == '__main__':
    unittest.main()
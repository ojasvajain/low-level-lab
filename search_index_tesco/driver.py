from search_index import SearchIndex
from document import Document


def drive():
    # Create docs
    search_index = SearchIndex()
    search_index.add_doc(Document(1, 'Amul Milk'))
    search_index.add_doc(Document(1, 'Amul Milk'))
    search_index.add_doc(Document(2, 'Nandini Chocolate Milk'))
    search_index.add_doc(Document(3, 'Milk Chocolate'))
    search_index.add_doc(Document(4, 'Chocolate Milk'))
    search_index.add_doc(Document(5, 'Milky Way Chocolate Bar'))

    docs = search_index.get_search_results('Chocolate Milk')
    for doc, score in docs:
        print(doc, score)


if __name__ == '__main__':
    drive()
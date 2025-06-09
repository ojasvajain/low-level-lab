

class SearchIndex:
    def __init__(self):
        self.inverted_index = dict()  # key = word, value = list of docs

    def add_doc(self, doc):
        words = doc.content.strip().split(' ')
        for word in words:
            token = word.lower()
            if token in self.inverted_index:
                self.inverted_index[token].append(doc)
            else:
                self.inverted_index[token] = [doc]
        print(f'Document {doc.id} added successfully')

    def get_search_results(self, query):
        words = query.strip().split(' ')
        matching_docs_set = {}
        is_first = True
        for word in words:
            token = word.lower()
            if token not in self.inverted_index:
                return []
            curr_docs = {doc for doc in self.inverted_index[token]}
            if is_first:
                matching_docs_set = curr_docs
                is_first = False
            else:
                matching_docs_set = matching_docs_set.intersection(curr_docs)

            if len(matching_docs_set) == 0:
                return []

        result_docs = list(matching_docs_set)
        for i in range(0, len(result_docs)):
            result_docs[i] = (result_docs[i], self.calc_match_score(query, result_docs[i].content))

        result_docs.sort(key=lambda x: x[1], reverse=True)
        return result_docs

    def calc_match_score(self, query, content):
        match = 0
        for ch in query:
            if ch in query:
                match += 1

        return int(100 * (match/len(content)))














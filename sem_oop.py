import math


class CountVectorizer:
    """gets unique words from input, creates document-term matrix"""

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self.stop_words = ("the", "a", "and")
        self._vocabulary = {}

    def fit_transform(self, input):
        """learns vocabulary dictionary, returns document-term matrix"""
        output = []
        max_i = 0
        for i, line in enumerate(input):
            if i != 0:
                output.append([0 for i in range(len(output[i-1]))])
            else:
                output.append([])
            for word in line.split():
                if self.lowercase:
                    word = word.lower()
                if word not in self.stop_words:
                    if word not in self._vocabulary:
                        self._vocabulary[word] = max_i
                        for elem in output[:-1]:
                            elem.append(0)
                        max_i += 1

                        output[i].append(1)
                    else:
                        output[i][self._vocabulary[word]] += 1
        return output

    def get_feature_names(self):
        """returns unique words from input"""
        return self._vocabulary.keys()


def tf_transform(count_mat):
    tf = []
    for elem in count_mat:
        sum_line = sum(elem)
        tf.append([round(i/sum_line, 3) for i in elem])
    return tf


def idf_transform(count_mat):
    idf = []
    docs_num = len(count_mat)
    for elem in range(len(count_mat[0])):
        cnt = 0
        for line in range(docs_num):
            if count_mat[line][elem] != 0:
                cnt += 1
        idf.append(round(math.log((docs_num + 1)/(cnt + 1)), 1) + 1)
    return idf


class TfidfTransformer:

    def fit_transform(self, count_mat):
        tf = tf_transform(count_mat)
        idf = idf_transform(count_mat)
        tfidf = []
        for line in tf:
            tfidf.append([])
            for i, elem_idf in enumerate(idf):
                elem_tf = line[i]
                tfidf[-1].append(round(elem_tf*elem_idf, 3))
        return tfidf


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        self._transformer = TfidfTransformer()
        super().__init__()

    def fit_transform(self, corpus):
        matrix = super().fit_transform(corpus)
        return self._transformer.fit_transform(matrix)


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)

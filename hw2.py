class CountVectorizer:
    """gets unique words from input, creates document-term matrix"""
    stop_words = ("the", "a", "and")

    def __init__(self, input=None, lowercase=True):
        if type(input) == list:
            self.input = input
        else:
            raise ValueError
        self.lowercase = lowercase
        self._vocabulary = {}

    def fit_transform(self):
        """learns vocabulary dictionary, returns document-term matrix"""
        output = []
        max_i = 0
        for i, line in enumerate(self.input):
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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
        'pasta pasta pasta pasta pasta pasta pasta pasta pasta'
        ]
    vectorizer = CountVectorizer(input=corpus)
    count_matrix = vectorizer.fit_transform()
    print(vectorizer.get_feature_names())
    print(count_matrix)

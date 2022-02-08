import re
from sklearn import svm
from random import shuffle
from extras import feelings, stemmer, result
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

dataset = []

stop_words = []
negation = []

probabilities = [0]*(2*len(feelings)-1)

with open('dataset/stopwords.txt', encoding="utf8") as file:
    stop_words = file.read().split()

with open('dataset/negation.txt', encoding="utf8") as file:
    negation = file.read().split()

for item in feelings:
    fileName = 'dataset/' + feelings[item] + '.txt'

    with open(fileName, encoding="utf8") as file:
        data = file.read()
        lines = data.split('\n')

        for line in lines:

            if line == "":
                continue
            try:
                pos = re.search('[0-9]', line).start()

                keywords = line[:pos]

                for word in keywords:
                    dataset.append([keywords, item])
            except:
                pass

shuffle(dataset)

X = [elem[0] for elem in dataset]  # keywords
Y = [elem[1] for elem in dataset]  # feeling numbers

vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(X)
X = X.toarray()

classifier = GaussianNB()
classifier.fit(X, Y)

punjabi = ''

with open('inputFile.txt', encoding="utf8") as file:
    punjabi = file.read()
    if punjabi == '':
        print('No input !')
        exit()

punjabi_lines = re.split('[।?!;.\n]', punjabi)
punjabi_lines = list(filter(lambda line: line != '', punjabi_lines))

for line in punjabi_lines:
    neg = False

    words = re.split("[,\"\' ]", line)
    words = list(filter(lambda word: word not in stop_words, words))
    words = list(map(stemmer, words))

    if any([(word in negation) for word in words]):
        neg = True

    pun = ' '.join(words)

    x = [pun]
    x = vectorizer.transform(x)
    x = x.toarray()

    group = classifier.predict(x)
    group = group[0]

    if group == 7:
        probabilities[group-1] += 1
    else:
        if neg == True:
            probabilities[2*group-1] += 1
        else:
            probabilities[2*group-2] += 1

total = sum(probabilities)
probabilities = list(map(lambda x: x/total, probabilities))

for i, feel in enumerate(result):
    print(feel + " : " + str(probabilities[i]))

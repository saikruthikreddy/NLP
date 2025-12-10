import nltk
from nltk.corpus import stopwords
from collections import defaultdict, Counter
nltk.download('punkt')

text = "I like apples and I like oranges"
stop = set(stopwords.words("english"))

words = [w for w in nltk.word_tokenize(text.lower()) if w not in stop]

bigrams = list(nltk.bigrams(words))
model = defaultdict(list)

for w1, w2 in bigrams:
    model[w1].append(w2)

word = "like"
print("Next-word prediction:", Counter(model[word]).most_common(1)[0][0])

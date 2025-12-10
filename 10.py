import nltk
from collections import Counter
nltk.download('punkt')

docs = [
    "i like car",
    "i like bike",
    " i like bus" ]

all_words = []
for d in docs:
    all_words += nltk.word_tokenize(d.lower())

bigrams = list(nltk.bigrams(all_words))
freq = Counter(bigrams)

print("Total bigrams:", len(freq))
print("Top 5:", freq.most_common(5))

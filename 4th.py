import matplotlib.pyplot as plt
from collections import Counter
import nltk
nltk.download('punkt')

text = "apple mango apple orange mango apple grape"
words = nltk.word_tokenize(text)
freq = Counter(words)

plt.bar(freq.keys(), freq.values())
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()

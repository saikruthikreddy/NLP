import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
nltk.download("punkt")
nltk.download("stopwords")

text = "@john I love NLP! @alice said it is awesome!!! #nlp"

handles = re.findall(r"@\w+", text)
print("Handles:", handles)

words = nltk.word_tokenize(text.lower())
stop = set(stopwords.words("english"))

clean = [w for w in words if w.isalpha() and w not in stop]

freq = Counter(clean).most_common(5)

plt.bar([w for w, c in freq], [c for w, c in freq])
plt.show()

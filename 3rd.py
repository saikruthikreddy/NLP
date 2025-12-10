import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

text = "This product is really good and worth the price."

tokens = nltk.word_tokenize(text)
stop = set(stopwords.words("english"))
ps = PorterStemmer()

clean = [ps.stem(w) for w in tokens if w.lower() not in stop]

print("Tokens:", tokens)
print("After Preprocessing:", clean)

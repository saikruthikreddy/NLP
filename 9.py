import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def get_pos(tag):
    if tag.startswith('J'): return wordnet.ADJ
    if tag.startswith('V'): return wordnet.VERB
    if tag.startswith('N'): return wordnet.NOUN
    if tag.startswith('R'): return wordnet.ADV
    return wordnet.NOUN

text = "The cats are running quickly and the dogs were playing."

lemm = WordNetLemmatizer()

tokens = nltk.word_tokenize(text)
pos = nltk.pos_tag(tokens)

lemmatized = [lemm.lemmatize(w, get_pos(p)) for w, p in pos]

print("Original:", text)
print("POS Tags:", pos)
print("Lemmatized:", " ".join(lemmatized))

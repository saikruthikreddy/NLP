import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt_tab')  # Added to resolve the LookupError
nltk.download('averaged_perceptron_tagger_eng')  # Added to resolve the new LookupError

# Sample Text
text = "i like cars and bikes"

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to convert NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ  # Adjective
    elif tag.startswith('V'):
        return wordnet.VERB  # Verb
    elif tag.startswith('N'):
        return wordnet.NOUN  # Noun
    elif tag.startswith('R'):
        return wordnet.ADV  # Adverb
    else:
        return wordnet.NOUN  # Default to noun

# Tokenize and POS Tagging
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

# Perform POS-based Lemmatization
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]

# Output Results
print("\nOriginal Text:")
print(text)
print("\nPOS Tags:")
print(pos_tags)
print("\nLemmatized Text (POS-Based):")
print(" ".join(lemmatized_words))

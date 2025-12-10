import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The cat sat on the mat"

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

print(tags)

# Simple parse tree
grammar = "S: {<DT><NN><VBD><IN><DT><NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(tags)
tree.draw()

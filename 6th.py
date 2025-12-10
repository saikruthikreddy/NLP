from collections import Counter

sentence = "I eat apples I eat mango"
words = sentence.split()

freq = Counter(words)
V = len(freq)

target = "eat"
prob = (freq[target] + 1) / (len(words) + V)

print("Laplace Probability of 'eat':", prob)

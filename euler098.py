from math import sqrt
from itertools import permutations

def is_square(n):
    return sqrt(n) % 1 == 0

def f(w1, w2):
    pass

infile = open("p098_words.txt", "r")
word_list = infile.readline().split(',')

word_dict = {i: [] for i in xrange(1, 15)}
for word in word_list:
    word_dict[len(word) - 2].append(word[1:-1])

anagram_sets = []
for i in xrange(1, 15):
    l = word_dict[i]
    for n in l:
        for m in l:
            if sorted(n) == sorted(m):
                if n != m:
                    if (m, n) not in anagram_sets:
                        anagram_sets.append((n, m))
anagram_sets = anagram_sets[::-1]
for anagram in anagram_sets:
    word1 = anagram[0]
    word2 = anagram[1]
    #f(word1, word2)

print anagram_sets
f('RACE', 'CARE')

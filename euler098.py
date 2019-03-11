from itertools import permutations
from eulertools import is_square

def max_square(anagram_pair):
    s1, s2 = anagram_pair
    letters = sorted(list(set(s1)))
    l = len(letters)
    max_val = 0
    if l <= 10:
        for tup in permutations([str(i) for i in range(10)], l):
            number_s1 = s1
            number_s2 = s2
            for i in xrange(l):
                number_s1 = number_s1.replace(letters[i], tup[i])
                number_s2 = number_s2.replace(letters[i], tup[i])
            if number_s1[0] != "0" and number_s2[0] != "0":
                if is_square(int(number_s1)) and is_square(int(number_s2)):
                    max_val = max(max_val, int(number_s1), int(number_s2))
    return max_val

def main():
    infile = open("./input/p098_words.txt", "r")
    word_list = [word[1:-1] for word in infile.readline().split(',')]

    anagram_pairs = []
    for word in word_list:
        for new_word in word_list:
            if new_word != word:
                if sorted(new_word) == sorted(word):
                    if (new_word, word) not in anagram_pairs:
                        anagram_pairs.append((word, new_word))
    anagram_pairs = sorted(anagram_pairs, key = lambda x: len(x[0]), reverse = True)
    return max(max_square(pair) for pair in anagram_pairs)

print main()

#Project Euler 54: Poker hands
card_ranks = "23456789TJQKA"

def value(hand):
    numbers = [card_ranks.find(card[0]) for card in hand]
    sort_nums = sorted(numbers)
    straight = all(sort_nums[i]-1 == sort_nums[i-1] for i in xrange(1,5))
    flush = all(x[1] == hand[0][1] for x in hand)
    #Check for straight flush (== royal flush)
    if straight and flush:
        return (9, max(numbers))
    #Four of a kind + Full House
    if len(set(numbers)) == 2:
        for i in numbers:
            if numbers.count(i) == 4:
                x = set(numbers)
                x.remove(i)
                return (8, [i] + list(x))
        for j in numbers:
            if numbers.count(j) == 3:
                x = set(numbers)
                x.remove(j)
                return (7, [j] + list(x))
    #Flush
    if flush:
        return (6, list(reversed(sort_nums)))
    #Straight
    if straight:
        return (5, max(numbers))
    #Three of a kind
    for i in numbers:
        if numbers.count(i) == 3:
            x = set(numbers)
            x.remove(i)
            return (4, [i] + sorted(x, reverse=True))
    #Two pairs
    for i in set(numbers):
        if numbers.count(i) == 2:
            y = set(numbers)
            y.remove(i)
            for j in y:
                if numbers.count(j) == 2:
                    x = set(y)
                    x.remove(j)
                    return (3, sorted([i, j], reverse=True) + list(x))
    #One pair
    for i in set(numbers):
        if numbers.count(i) == 2:
            x = set(numbers)
            x.remove(i)
            return (2, [i] + sorted(x, reverse=True))
    #High card
    return (1, list(reversed(sort_nums)))

with open("../input/p054_poker.txt", "r") as infile:
    print sum(value(line.split()[:5]) > value(line.split()[5:]) for line in infile)

#The really big thing we use here is that Python does element-wise comparison
#on tuples and lists from left to right. So we have (9, x) > (8, y) regardless
#of what x and y are. Thus we can assign a tuple-based value to all hands in
#such a way that hand1 > hand2 if hand1 beats hand2.

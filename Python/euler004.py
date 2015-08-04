#Project Euler 4: Largest palindrome product

def is_palindrome(n):
    """Checks if a number is palindrome"""
    return str(n) == str(n)[::-1]

products = sorted([i*j for i in xrange(100, 1000) for j in xrange(100, 1000)], reverse=True)
#All products of 3-digit numbers, sorted by largest first
for product in products:
    if is_palindrome(product):
        #The moment we find a palindrome, it will be maximal.
        print product
        break

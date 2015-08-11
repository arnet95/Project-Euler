squareSum n = sum([i^2 | i <- [1..n]])
sumSquare n = sum([i | i <- [1..n]])^2

sumSquareDifference n = sumSquare n - squareSum n

main = print(sumSquareDifference 100)

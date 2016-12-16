squareSum n = sum(map (\x -> x^2) [1..n])
sumSquare n = sum([1..n])^2

sumSquareDifference n = sumSquare n - squareSum n

main = print(sumSquareDifference 100)

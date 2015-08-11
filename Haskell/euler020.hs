digitSum n
    | n < 10 = n
    | otherwise = rem n 10 + digitSum (quot n 10)

factorial n
    | n == 0    = 1
    | otherwise = n * factorial (n-1)

main = print(digitSum(factorial(100)))

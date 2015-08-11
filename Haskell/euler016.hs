digitSum :: Integer -> Integer
digitSum n
    | n < 10 = n
    | otherwise = rem n 10 + digitSum (quot n 10)

main = print (digitSum (2^1000))

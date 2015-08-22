digitSum :: Integer -> Integer
digitSum n
    | n < 10 = n
    | otherwise = mod n 10 + digitSum (div n 10)

main = print (digitSum (2^1000))

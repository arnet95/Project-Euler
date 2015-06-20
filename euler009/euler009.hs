main = print ( product (head [[a, b, c] | a <- [1..333], b <- [a+1..500], c <- [b..a+b], a^2 + b^2 == c^2, a + b + c == 1000]))

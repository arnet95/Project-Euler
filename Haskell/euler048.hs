pow n x m
    | x == 0    = 1
    | otherwise = rem (n * (rem (pow n (x-1) m) m)) m

main = print(rem (sum (map (\n -> pow n n (10^10)) [1..1000])) (10^10))

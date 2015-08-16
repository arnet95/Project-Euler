pow n x m
    | x == 0    = 1
    | otherwise = mod (n * (mod (pow n (x-1) m) m)) m

main = print(mod (sum (map (selfPow m) [1..1000])) m)
    where selfPow m n = pow n n m
          m = 10^10

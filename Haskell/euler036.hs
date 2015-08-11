palindrome b n = reversal b n == n

reversal base = go 0
  where go a 0 = a
        go a b = let (q,r) = b `quotRem` base in go (a*base + r) q

main = print (sum (filter (\n -> palindrome 10 n && palindrome 2 n) [1..10^6]))

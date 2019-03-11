is_palindrome(n) = string(n) == reverse(string(n))
euler004 = maximum(i*j for i = 100:999, j = 100:999 if is_palindrome(i*j))
println(euler004)

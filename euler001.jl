euler001(n) = sum(x for x in 1:n-1 if x % 3 == 0 || x % 5 == 0)
println(euler001(1000))

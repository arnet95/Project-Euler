sum_of_squares(n) = sum(i^2 for i in 1:n)
square_of_sum(n) = sum(i for i in 1:n)^2
euler005(n) = square_of_sum(n) - sum_of_squares(n)
println(euler005(100))

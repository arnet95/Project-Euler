memoized_fib :: Int -> Integer
memoized_fib = (map fib [0 ..] !!)
   where fib 0 = 0
         fib 1 = 1
         fib n = memoized_fib(n-2) + memoized_fib(n-1)

fibonaccis = (map memoized_fib [0..])
evenFibonaccisToLimit n = (filter even (takeWhile (< n) fibonaccis))
main = print(sum (evenFibonaccisToLimit 4000000))

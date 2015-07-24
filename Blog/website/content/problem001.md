Title: Problem 1
Date: 2015-07-02
Category: Problem solutions

####Problem text

####Solution idea
Since we only need to check numbers up to 1000, this is a problem which is within the scope of a brute-force approach, and in order to check for divisibility we can use the [modulo operator](https://en.wikipedia.org/wiki/Modulo_operation).

Here is a possible solution which is very straightforward:

	:::python
	def problem1(n):
	    s = 0
	    for i in xrange(1, n):
	        if i%3 == 0 or i%5 == 0:
	            s += i
	    return s

####Other (similar) solutions

#####Python one-liner

	:::python
	print sum(i for i in xrange(1, 1000) if i%3 == 0 or i%5 == 0)

#####Scheme

	:::scheme
	(define (range start stop)
  	  (if (= start stop)
	    '()
	    (cons start (range (+ start 1) stop))))

	(define (divisible-by n m)
	  (= 0 (modulo n m)))

	(define (filter pred lst)
	  (cond ((null? lst) '())
	        ((pred (car lst)) (cons (car lst) (filter pred (cdr lst))))
	        (else (filter pred (cdr lst)))))
      
	(apply + (filter 
          (lambda (n) 
            (or (divisible-by n 3)
                (divisible-by n 5)))
          (range 1 1000)))

#####Haskell
	:::haskell
	main = print (sum [x | x <- [1..999], mod x 3 == 0 || mod x 5 == 0])

####Efficiency
For this small limit, the 

	

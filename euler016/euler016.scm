(define (digit-sum n)
  (if (< n 10)
      n
      (+ (modulo n 10) (digit-sum (quotient n 10)))))

(digit-sum (expt 2 1000))
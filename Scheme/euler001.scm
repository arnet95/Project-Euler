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

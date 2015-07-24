(define (factorise num)
    (define (fact-sub i n)
      (cond ((= i n) (cons i '()))
            ((= 0 (modulo n i)) (cons i (fact-sub i (/ n i))))
            (else (fact-sub (+ i 1) n))))
    (fact-sub 2 num))

(apply max (factorise 600851475143))

#lang racket

(define l1 (list 4 5 72 1 5))
(car l1) ; 4
(cdr l1) ; '(5 72 1 5)
(cadr l1); 5
(cddr l1); '(72 1 5)
(caddr l1);; 72
(cddddr l1); '(5) ; there isn't more functions like cdd...dr !
(null? l1) ; #f -> isn't empty

(define (sum xs)
  (if (null? xs)
      0
      (+ (car xs) (sum (cdr xs))))) ; sum of all members(numbers) in the list

(define (my-append xs ys)
    (if (null? xs)
        ys
        (cons (car xs) (my-append (cdr xs) ys))))

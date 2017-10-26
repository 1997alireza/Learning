#lang racket

(string? "asd") ; -> #t
(string? 23); -> #f

(define x 2)
(equal? x 2); -> #t

(define 3*2 (* 3 2))
;identifiers can have any characters in the name but ()[]{}",'`;#|\

(define (add-two x) (+ x 2))

(real? 2+1/2i)
(integer->char 23)

(eq? 0.1 1/10) ; #f

(let ((x 2)) (eqv? x 2)) ; #t


(lambda (x) (+ x 2)); anonymous function


(define (sum a b) 
  (define (suma c) ; internal define
    (+ a c))
  (suma b))

(define num -0)
(cond
  [(not (real? num)) "NaN"]
  [(> num 0) "Pos"]
  [(< num 0) "Neg"]
  [else "Zero"])
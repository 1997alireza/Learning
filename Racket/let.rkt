#lang racket

(let ([x 2] [y (+ 2 1)]) (+ x y)) ; 5
(let* ([x 2] [y (+ x 1)]) (+ x y)) ; 5
(letrec ([is-even? (lambda (n)
                       (or (zero? n) 
                           (is-odd? (sub1 n))))]
           [is-odd? (lambda (n)
                      (and (not (zero? n))
                           (is-even? (sub1 n))))])
    (is-odd? 11))

#| In a "let*", the first bindings are available to the next ones.

In "letrec", all bindings are available to each other (mainly for mutually
recursive local functions) |#

(define x 3)
(define y 2)
(let ([x y] [y x])(cons x y)) ; reverse x and y just for its body

(define (sum x)
(let sum-help ([x x] [res 0])
(cond [(= x 0) res]
[else (sum-help (sub1 x) (+ res x))])))
#| We can set name for a let statement. 
so we have a internal function and we can call it in itself recursive.
and when we call it in itself we must set its arguments but the first time we have initial values. |#

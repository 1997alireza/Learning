#lang racket

(provide (all-defined-out))

(define x 2); it's a comment!

(define y(+ x 2)); y is 4

(define cube1 (lambda (x) (* x (* x x))))
(define cube2 (lambda (x) (* x x x)))
(define (cube3 x) (* x x x))

(define (pow1 x y)
  (if (< y 1)
      1
      (* x (pow1 x (- y 1)))))
(define pow2 (lambda (x)
               (lambda (y)
                 (pow1 x y))))
(define (powTo2 x) (pow1 x 2))
(define (pow2ToX) (pow2 2)); call: ((pow2ToX)3)


(define (say something) 
  (printf "Hi\n")
  (string-append something"!"))
;you can call the function like this: (say "...") #with parentheses

(define (ext str) (substring str 4 0))

(define (plus1 x y) ; call: (plus1 x y)
  (+ x y))

(define p2 ; call: (p2 x)
  (lambda (x)
    (+ 2 x)))

(define plus2 ; call: ((plus2 x)y)
  [lambda (x)
    (lambda (y)
      (+ y x))])



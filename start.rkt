#lang racket

(define x 2); it's a comment!

(define y(+ x 2)); y is 4

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
  (lambda (x)
    (lambda (y)
      (+ y x))))
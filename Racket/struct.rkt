#lang racket

(struct foo (bar baz) #:transparent)
; ransparent is useful when a 'foo struct print in REPL(Read Eval Print Loop)

(define x (foo 'a 'b))
; if foo is #'transparent : x -> (fpp 'a 'b) ,else : x -> #<foo>

(foo? x) ; #t
(foo-bar x) ; 'a
(foo-baz x) ; 'b

;-------------------
; we can have mutable structs

(struct car (model color) #:mutable #:transparent)
; now we have two extra functions: set-car-model! and set-car-color!

(define aCar (car 'lamborghini 'red))
(set-car-color! aCar 'blue) ; aCar -> (car 'lamborghini 'blue)
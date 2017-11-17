#lang racket

(define x 'x)
(define y 'y)

(set! x y) ; x -> 'y; mutation


; begin allow us to have sequencing; useful when we have side-effects
(define (seqFunc)(begin
  (define z 10)
  z)) ; -> 10

;------------------------
(define b 3)

(define f (lambda (x) (+ x b)))
; it will be evaluated when its called; so when we call 'f we have updated value of 'b

(define c (+ b 4)) ; 7
; but this evaluate now and when we use 'c its independent of updated value of 'b 

(set! b 5)
(define z (f 4)) ; 9
(define w c) ; 7

;-----------------------
; it can make mistake for us that 'set! can change anything
; we can make a local copy
(define e 1)
(define f2
  (let ([e e])
    (lambda (x) (+ x e)))) ; have a local variable named 'e and it can't be chaned from out of it's block
(set! e 10)
(define z2 (f2 4)); 5

; warning!: the functions and primitives can be changed! so...:
(define f2_new
  (let ([e e] [+ +] [* *])
     (lambda (x) (+ x e)))) ;
(set! e -1)
(define z3 (f2_new 2)); 12

;-----------------------
;but it seems so dirty coding! :/
;if a module does not use 'set! on a top-level variable, racket makes it constant
;  and forbids 'set! outside the module. so local variables like those doesn't necessary :)
#lang racket

(define (atom? x)
  (not (or (pair? x) (null? x))))

(define substitute (lambda (repExp var mainExp)
                     (if (null? mainExp) null 
                         [if (atom? mainExp)
                             [if (eq? mainExp var) repExp mainExp]
                              (cons
                               (substitute repExp var (car mainExp))
                               (substitute repExp var (cdr mainExp))
                              )
                         ]
                     )
                   ))
; (substitute '5 'x '(+ x 2)) -> '(+ 5 2)

(define (subst&eval repExp var mainExp)
  (eval (substitute repExp var mainExp)))
; (subst&eval '5 'x '(+ x 2)) -> 7
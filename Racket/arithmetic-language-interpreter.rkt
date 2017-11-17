#lang racket

; we can create struct for having datatype
(struct const (int) #:transparent)
(struct negate (e) #:transparent)
(struct add (e1 e2) #:transparent)
(struct multiply (e1 e2) #:transparent)

; simple interpreter: it takes AST(abstract syntax tree) and runs the program
(define (eval-exp e)
  (cond [(const? e) e]
        [(negate? e) (const (- (const-int (eval-exp (negate-e e)))))]
        [(add? e) (const (+ (const-int (eval-exp (add-e1 e)))
                           (const-int (eval-exp (add-e2 e)))
                        )
                 )]
        [(multiply? e) (const (* (const-int (eval-exp (multiply-e1 e)))
                           (const-int (eval-exp (multiply-e2 e)))
                        )
                 )]
        [true (error e "unknown symbol")]))

; test
(define result (eval-exp 
  (multiply (negate (add (const 2) (const 4))) (const 3))) )
; result -> (const -18)
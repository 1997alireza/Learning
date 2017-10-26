#lang racket

(random 3); generate random integer between 0 and 3

(define pair (cons 1 2))
(car pair); 1
(cdr pair); 2

(define p2 (cons 1 (cons 2 3)))
(car (cdr p2)); 2

#; (let loop() (loop)) ; This creates a function called loop and executes it

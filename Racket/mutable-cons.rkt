#lang racket

; we want to mutate the contents of a cons cell
(define x (cons 14 null))
(define y x)
(eq? y x) ; #t
(set! x (cons 42 null)); it's bot mutating and by set! 'x will be an another cons
(eq? y x) ; #f
(car y) ; is 14 and isn't 42

;------------- mutable cons -> mcons
(define mx (mcons 14 null))
(define my mx)
(eq? my mx) ; #t
(set-mcar! mx 42)
(eq? my mx) ; #t
(mcar my) ; 42 like (mcar mx)

(mpair? my); #t

(mcdr mx); '() 
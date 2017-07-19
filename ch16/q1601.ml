
(* 16.1
 * Number Swapper
 *
 * Write a function to swap a number in place
 * (that is, without temporary variables).
 *)


let sol1 (x : int ref) (y : int ref) : unit =
  (  x := !x lxor !y
  ;  y := !x lxor !y
  ;  x := !x lxor !y
  )
;;


let sol2 (x : int ref) (y : int ref) : unit =
  (  x := !x - !y
  ;  y := !x + !y
  ;  x := !y - !x
  )
;;


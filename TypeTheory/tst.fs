module Ex01a

type filename = string

(** [canWrite] is a function specifying whether a file [f] can be written *)
let canWrite (f:filename) = 
  match f with 
    | "demo/tempfile" -> true
    | _ -> false

(** [canRead] is also a function ... *)
let canRead (f:filename) = 
  canWrite f               (* writeable files are also readable *)
  || f="demo/README"       (* and so is demo/README *)
open Core

let rec solve l = match l with
  | prev::cur::r -> (Int.compare prev cur)::(solve (cur::r))
  | _ -> []

let rec slide3 l = match l with
  | fst::snd::lst::r -> (fst+snd+lst)::(slide3 (snd::lst::r))
  | _ -> []

let () =
  let lines = In_channel.read_lines "input.txt" in
  let lines = List.map ~f: int_of_string lines in
  let lines = slide3 lines in
  let off = solve lines in
  print_string (string_of_int (List.count ~f: (fun v -> v = -1) off))

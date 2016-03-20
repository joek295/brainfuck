[

fibonacci number generator

Prints the fibonacci sequence.  Non-terminating.  Code for outputting
the value of a cell as a number comes from esolangs.org's Brainfuck
Algorithms page.

]

+++++ +++++ > 10  0  0
>>>+>+      10  y  x

[

printing code
[>>+>+<<<-]>>>[<<<+>>>-] copy cell to print into temp cell
                         10 y  x  0  x  0*
<<+>                     10 y  x  1  x* 0
[<->[>++++++++++<[->-[>+>>]>[+[-<+>]>+>>]<<<<<]>[-]++++++++[<++++++>-]>[<<+>>-]>[<<+>>-]<<]>]
<[->>++++++++[<++++++>-]]
<[.[-]<]

<<<<< < . >>>>>

[-<<+<+>>>]<[->+<]<[->>+<<]<[->>+<<]>>>

]

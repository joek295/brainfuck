[
fibo.bf: a fibonacci number generator.

]

+++++ >
+++++ +++++ >

+ > + <

10 10 1! 1 0 0 etc

++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++
.
< . > 
.
< . >
---------- ---------- ---------- ---------- --------

< <

[

    - > >

    > [ - > + > + < < ]

    10 10 1 0! 1 1

    > [ - < + > ] 
    > [ - < < < + > > > ] 

    10 10 2 1 0 0!

    < < <

    ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++
    .
    < . >
    ---------- ---------- ---------- ---------- --------

    10 10 2! 1 0 0

    [ - > + > + < < ] > > [ - < < + > > ]

    <

    ++++++++++ ++++++++++ ++++++++++ ++++++++++ ++++++++
    .
    << . >>
    ---------- ---------- ---------- ---------- --------

    < < <

]

[

Currently, this generates cells with fibonacci numbers, and then
naively adds 48 to them and prints, which only works if the number is
between 0 and 9, which is only true of the first six fibonnaci
numbers.

It also breaks completely for any number larger than 78.

]

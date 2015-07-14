# The Brainfuck Progamming Language:

Brainfuck is an esoteric programming language with a limited
instruction set of eight discrete instructions, each represented as a
single character.  Brainfuck instructions operate on a (theoretically)
infinitely long tape, consisting of cells which hold an integer value
of (again theoretically) any size.

These instructions are:

* increment the value of the cell under the pointer (+)

* decrement the value of the cell under the pointer (-)

* move the pointer one cell to the right (>)

* move the pointer one cell to the left (<)

* output the value of the cell under the pointer as an ASCII character
  (.)

* read a single byte of input, and store its value in the cell under
  the pointer (,)

* if the cell under the pointer has a value of zero, jump forward in
  the instructions to the matching ] ([)

* if the cell under the pointer does not have a value of zero, jump
  backwards in the instructions to the matching [ (])

Despite this, brainfuck is a Turing-complete language, which means that given
enough time and computing power, it can do anything that any other
Turing-complete language can do (or, formally, can calculate any
Turing-computable function, or simulate a Universal Turing Machine).

In practice, due to limitations in computing power, most interesting
functions of Turing machines are prohibitively expensive in languages
such as brainfuck.  Additionally, the difficult-to-read syntax, and
difficulty of writing code due to the lack of useful functions, makes
brainfuck mostly a toy language.

# The Brainfuck Interpreter:

The brainfuck interpreter is relatively simple, and many
implementations exist online.  The core of the version available here
was written in Python over the course of two days, and less than two
hours of coding time.

Because brainfuck is an underspecified language, there are various
design decisions that have to be made when writing an interpreter or a
compiler.

## Cell Size:

The original brainfuck implementation had cells limited to 8 bits.
Other implementations have used 16-bit, 32-bit, 64-bit and bignum
cells.  This interpreter uses python's integers, which are 64 bits on
my 64-bit Debian system, but 32 bits on some other systems.

## Tape Size:

The tape is set at 30,000 cells, which is identical to the original
brainfuck implementation.  Also matching the original implementation,
the pointer is set to be at the leftmost cell.  When moving the
pointer out of the tape to the left, it wraps to the end of the tape.
When moving the pointer out of the tape to the right, behaviour is
undefined and there may be bugs.  Eventually, I plan to implement
dynamically increasing the size of the array when this occurs.

## Planned Features:

* Dynamic resizing of tape if the pointer moves beyond the 30,000th
  cell.

* If no code is given as an argument, act as an interactive
  interpreter.

* If no input is given and program tries to read input, ask for input
  on stdin.

* Warnings for unmatched [ and ]

# UNLICENCE:

The code for the brainfuck interpreter is [Unlicensed](unlicense.org)
and released into the public domain.  The Unlicense text can be found
in the UNLICENSE file.

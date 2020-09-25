### Conway's Game of Life is a simulation of what happens when a certain cell:

* is overpopulated
* is underpopulated
* is dead
* is revived/reproduced

# Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.


Some crazy things can take place in this simulation, some cells decay very slowly, some that die almost instantly only to be revived in a later generation. Some cells continually transform and morph into new things, all of this based on the defined rules that every cell must follow.

<hr>

This iteration tracks the age of the cell, and the color of the cell changes to represent the age, some colors changes are subtle and some are more drastic, this is to easily identify the oldest/youngest of the cells in the simulation, a key follows to keep track of the age:

* Youth: green
* Prime: red
* Middle Age: deep blue
* Old Age: bright blue

When a cell reaches a certain age, it dies and a new cell is immediately born in its place, continuing the circle of life.

# Conway's Game of Life with pygame/Python

<a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Wikipedia reference</a>

Conway's Game of Life meets the criteria of always being in one state which is an
element in a set of predefined, finite states. The head is also always in a single
location since we're in a run loop that only ends on the condition that we want
it to end (as it would be with turning off a machine)

<a href="https://en.citizendium.org/wiki/Turing_Machine">Turing reference</a>


# Some future goals:

* I would like to implement a speed adjustment, some kind of slider / up or down button that adjusts the speed of generation in real time during the simulation

* I want to deploy this on an iOS application, doing this in Python was a challenge and I want to apply this knowledge to my preferred language and platform!

* Create a dynamic screen window that full screens/minimizes based on the user's resolution

* Create preset seeds in a drop-down window or something.




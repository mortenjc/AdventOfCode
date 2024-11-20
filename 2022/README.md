# Advent of Code 2022
Some solutions to the Advent of Code challenge (https://adventofcode.com/)

## YouTube videos of selected solutions
After solving the puzzles I go and check videos of some
of the leaderboard contributers (often just picking the
first that comes up from the search). I do this to try to
learn about different approaches to attacking the problem,
language features I don't know and the use of additional
packages.

### Day 5
https://www.youtube.com/watch?v=Fg7wLU5xhQo

Interesting to see that he is super fast in solving the problem
because he skips parsing the graph and just manually copies it into a
relevant structure. Then struggles a bit to do the parsing.

https://www.youtube.com/watch?v=jMwr1Uc4g-o

Here I learned the trick to split data in two parts based on
a blank line (actually to consequetive newlines)

    .split('\n\n')

also learned about the pprint package and that I should definitely
look into string and list indexing

    [-1:] last entry
    [-n:] last n entries
    .extend()

### Day 6
https://www.youtube.com/watch?v=LvwsB-JpJmQ

Very fast and solved this with a 3-liner. Interesting enough he solved
the first problem in a very specific way and then had to generalise
for the second solution. Main take away points

    create the set and then check it has length n
    create sets backwards to simplify range checking

    if (len >= 3) and len(set(...)) == 4

### Day 7
https://www.youtube.com/watch?v=ZPM5xclRInk

My approach was the same, just took me a lot longer, but
I wasted time on a too complicated parser and also working
around =+ operations on non-existing keys. I also used a weird
logic to calculate dir names and removing the double '/' which
he just ignored. Main learnings:

    use defaultdict (from collections import defaultdict)
    sizes = defaultdict(int)

    sometimes list comprehension is not necessary

https://www.youtube.com/watch?v=YLHPABNNgZU

Also uses defaultdict and has an interesting idea to split
the input on '\n$' to a single line with the command and its
output.

### Day 8
https://www.youtube.com/watch?v=2lypi76wRsM

This took me a long time and the above solution was both
faster and more elegant. Learnings

Reading the input file directly into a useful structure as a oneliner

    grid = [list( map(int, line)) for line in open(ifile).read().splitlines()]

Using all([]) returns True if all elements are True -  in conjuntion with list comprehension

    if all(board[r][i] < h for i in range(c)):
        return True

Use builtin functions whenever possible. In this case max() rather two-line if statement

    best = max(val, best)


### Day 10
Learnings:

Maybe useful to avoid multi line if

    a = (A if X else B)  

Initialise 2D grid

    G = [['.' for _ in range(nx)] for _ in range(ny)]


### Day 14
Learnings/discoveries

    Use PIL for creating image

![Day 14](2022/day14/result.png)


### Day 21
Use 'exec' to create variables and solve by substitution

    exec(f'{name} == {val}')

where name and val are previously parsed strings.


### Day 24
Learned that Python's 'for' have an 'else' section

    for x in s:
        if ... :
            break
    else:
        didn't break


### Day 25
Reversing a list

    snafu[::-1]

or returning every n'the element (backwards or forwards)

    a[::3]
    a[::-2]

Discovered 'divmod'

    q, r = divmod(8,3)

For this week's exercise I want you to write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) with adjacent duplicate values removed.

For example:

>>> compact([1, 1, 1])
[1]
>>> compact([1, 1, 2, 2, 3, 2])
[1, 2, 3, 2]
>>> compact([])
[]

sequence - generic term for an ordered set. List, tuple, string. 

Bonus 1

For the first bonus, make sure you accept any iterable as an argument, not just a sequence (which means you can't use index look-ups in your answer). ✔️

Here's an example with a generator expression, which is a lazy iterable:

>>> compact(n**2 for n in [1, 2, 2])
[1, 4]
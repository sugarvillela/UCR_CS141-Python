## LocationCostPlan problem Description

Suppose you're running a lightweight consulting business just you, two
associates, and some rented equipment. Your clients are distributed between the East
Coast and the West Coast, and this leads to the following question.

Each month, you can either run your business from an offce in New York (NY) or
from an offce in San Francisco (SF). In month i, you'll incur an operating cost of Ni,
if you run the business out of NY, you'll incur an operating cost of Si if you run the
business out of SF. It depends on the distribution of client demands for that month.
However, if you run the business out of one city in month i, and then out of the other
city in month i + 1, then you incur a fixed moving cost of M to switch base offices.

Given a sequence of n months, a plan is a sequence of n locations, each one equal to
either NY or SF such that the ith location indicates the city in which you will be based
in the ith month. The cost of a plan is the sum of the operating costs for each of the n
months, plus a moving cost of M for each time you switch cities. The plan can begin in
either city.

The problem: Given a value for the moving cost M, and sequences of operating costs, 
find a plan of minimum cost. Such a plan will be called optimal.

## FitToMargins problem Description
In a word processor, the goal of \pretty-printing" is to take text with a
ragged right margin, like this,

Call me Ishmael.
Some years ago,
never mind how long precisely,
having little or no money in my purse,
and nothing particular to interest me on shore,
I thought I would sail about a little
and see the watery part of the world.

and turn it into text whose right margin is as even as possible, like this.

Call me Ishmael. Some years ago, never
mind how long precisely, having little
or no money in my purse, and nothing
particular to interest me on shore, I
thought I would sail about a little
and see the watery part of the world.

To make this precise enough for us to start thinking about how to write a pretty-printer
for text, we need to figure out what it means for-the right margins to be even. So sup-
pose our text consists of a sequence of words where wi consists of ci characters, we 
have a maximum line length of L. We will assume we have a fixed-width font and ignore 
issues of punctuation or hyphenation.

A formatting of W consists of a partition of the words in W into lines. In the words 
assigned to a single line, there should be a space after each word except the last. The 
difference between the left-hand side and the right-hand side will be called the slack of
the line, that is, the number of spaces left at the right margin.


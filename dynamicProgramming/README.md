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
In a word processor, the goal of "pretty-printing" is to take text with a
ragged right margin and turn it into text whose right margin is as even as possible.

To make this precise enough for us to start thinking about how to write a pretty-printer
for text, we need to figure out what it means for-the right margins to be even. So sup-
pose our text consists of a sequence of words where wi consists of ci characters, we 
have a maximum line length of L. We will assume we have a fixed-width font and ignore 
issues of punctuation or hyphenation.

A formatting of W consists of a partition of the words in W into lines. In the words 
assigned to a single line, there should be a space after each word except the last. The 
difference between the left-hand side and the right-hand side will be called the slack of
the line, that is, the number of spaces left at the right margin.

## Superposition of Two Strings problem description

You're consulting for a group of people (who would prefer not to be men-
tioned here by name) whose jobs consist of monitoring and analyzing electronic signals
coming from ship s in coastal Atlantic waters. They want a fast algorithm for a ba-
sic primitive that arises frequently: "untangling" a superposition of two known signals.
Specifically, theyre picturing a situation in which each of two ships is emitting a short
sequence of 0's and 1's over and over, and they want to make sure that the signal they're
hearing is simply an interleaving of these two emissions, with nothing extra added in.
Given a string x consisting of 0's and 1's, we write xk to denote k copies of x con-
catenated together. We say that a string x0 is a repetition of x if it is a prefix of xk for
some number k. So x0 = 10110110110 is a repetition of x = 101.

We say that a string s is an interleaving of x and y if its symbols can be partitioned
into two (not necessarily contiguous) subsequences s' and s'', so that s' is a repetition of
x and s'' is a repetition of y. (So each symbol in s must belong to exactly one of s' or s''.)
For example, if x = 101 and y = 00, then s = 1000101010 is an interleaving of x and y,
since characters 1,2,5,7,8,9 form 101101, a repetition of x, and the remaining characters
3,4,6,10 form 0000, a repetition of y.

In terms of our application, x and y are the repeating sequences from the two ships,
and s is the signal were listening to: We want to make sure s "untangles" into simple
repetitions of x and y.

## Edit Distance problem description

Take two strings like "EXPONENTIAL" and "POLYNOMIAL". They're similar, but how similar?  Specifically, how many steps would it take to line them up, or convert one into the other?  The pseudocode for this is in *Algorithms* (Dasgupta et al) on page 159.  I figured out how to make it work in Python.

## Non-Fractional Knapsack and others

Plenty of implementations of these are available. I wrote mine based on the pseudocode in instructor lectures.


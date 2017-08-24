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

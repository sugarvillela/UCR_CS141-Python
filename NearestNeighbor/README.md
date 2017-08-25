## Nearest Neighbor Problem Description

Input: A set of points in the plane

Output: The distance between the closest pair of points: that is, the pair pi != pj for which the distance between pi and pj is minimized.

#### Divide-and-Conquer Here's a high-level overview of the divide-and-conquer algorithm:

Find a value x for which exactly half the points have xi < x, and half have xi > x. On this basis, split the points into two groups L and R.

Recursively find the closest pair in L and in R. Say these pairs are pL, qL and pR, qR with distances dL and dR respectively. Let d be the smaller of these two distances.

It remains to be seen whether there is a point in L and a point in R that are less than distance d apart from each other. To this end, discard all points with xi < x - d or xi > x + d and sort the remaining points by their y-coordinate.

Now, go through this sorted list, and for each point, compute its distance to the subsequent points in the list. Let pM, qM be the closest pair found in this way.

#### Brute Force

You will also be implementing a brute force version of the algorithm which will compare all pairs of points to find the closest pair. This algorithm will be used for comparison purposes.

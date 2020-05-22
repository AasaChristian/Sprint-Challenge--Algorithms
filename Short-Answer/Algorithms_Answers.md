#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(1):
I chose this complexity because this function will run the same time for all positive numbers and once for all negative numbers.  


b)
O(n^2)
I chose this complexity because every i in range n has to go thru the while loop.


c)O(n)
This is function will run n number of times.

## Exercise II
The building floors would be a sorted list starting from 1(the first floor) to the top floor.

The plan is to divide the floors in half, and drop the egg from the middle floor
if the egg breaks, that would mean the egg will break in all the floors above it, so I throw out all the floors above
if the egg doesn't break I can assume that the egg wouldn't break on any floor below it, so I throw out all the floors below

If this process is iterated with the remanding list,
eventually you will be left with one floor




#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -- the while loop is executed {n} times. When a=0, it is O(1) while a < n * n * n, so it can be written as O(n) a = a + n * n O(n)

a = 0 --> O(1)
while a(a< n *n * n) --> O(n)
a = a + n * n --> O(1)

example:
n=2
0 < 8
4 < 8
8 < 8 stop


b) O(nlogn). the while loop is an innter loop executed n/2 times and an increment inside where j is multiplied by 2 means that j increments exponentially, so it scales to the inverse, and thus logn, and the while is a nested for loop executed n times. So you take the O(n) from the nested while loop and the O(logn) from the for loop to get O(nlogn) 





c) O(n). the amount of the bunnies recusrively increments by 2 in each recursion, so that means it is linear. if bunnies = 0, it returns 0 so is O(1) and thus 0(n)


## Exercise II

For this solution, I would use a binary search tree to solve it. 

First Step:
We would divide the building into two parts -- dividing in half first to see the floors where the egg breaks and floors where it doesn't break.

Second Step:
Continually testing to see if an egg breaks on floor of f, and if it breaks, divide the building tinto two parts and move to the middle of the lower floors. If it does break, divide into two parts and move to the middle of the upper floors.

Third Step:
Repeat step 2 until it resolves to find the floor where the maximum dropping height is. 

This method has a runtime complexity of O(log n)



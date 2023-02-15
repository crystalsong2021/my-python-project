"""
70. Climbing stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Method
1. recusion - which will excedeed the time limit
2. cache - stored the result of the repeating work
3. dynamic programming - bottom up
   Going backwards: if n is 5 , we will start from 4, 3, 2, 1,
   it's like fibnanci number, we are adding only the two value of the next two number
   instead of storing the whole array, we actually only need 2 value memory space
   0 1 2 3 4 5
           1 1 - (start with one, two 1, 1 as default)
         2
       3
     5
   8 (result)
"""

def climbing_stair(n):
    one, two = 1, 1
    for i in range(n-1, 0, -1):
        temp = one + two
        two = one
        one = temp
    return one

result = climbing_stair(3)
print(result)
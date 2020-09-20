"""




need the count of pair of songs that have a combine sum of multiple of 60 

ex = [40,20,60]
ans =  1

ex = [60,60,60]
ans = 3 

ex = [90, 150, 40, 20 ]
ans = 2

Brute force approach:

O(n2)

4, 2, 6

6 -4 = 2 in lit

60 - 40 = 20 in list

max list -> 60

60 * 1 or 60 * 2



ex 1= [40, 20, 60, 90]


i = 0,1,2
40, 20
j = 1,2,3

1. i = 40, j=20 count=1

0, 1
0, 2
0, 3

1, 2
1, 3

2, 3


 0,   1,   2,  3
[90, 150, 40, 20 ]


1.  90, 150 1
2, 90, 40  
3. 90, 20 

150,  40 0 \
150, 20 0

40, 20  1


60 * 3 % 60 = i
"""






nums = [40,20,60]
'''
final_count =0 
refedict = {}

i = 0 
tempNum = 20
rd = {40:1}

i = 1
tempNum = 40
fc  = 1
rd = {40:1, 20:1}

i = 2
tempNum = 60 
rfd

list = [60,60,60]

fc = 0
rd = {}

i = 0
tempNum = 60
rd ={60:1}



'''

from collections import defaultdict
def solution1(nums):
    if not nums:
        return None
    referenceDict = defaultdict(int)
    final_count =0 
    for i in range(len(nums)):
        tempNum =  (60-nums[i]%60)%60 # need to add something to cover a case when number is 60 
        if tempNum in referenceDict:
            final_count +=  referenceDict[tempNum]  
        if tempNum%60 == 0:
            referenceDict[60] += 1
        else:
            referenceDict[num[i]%60] += 1
    return final_count
'''
l = [60,60,60]

0,1,2,3,4, ..... 55,56,57,58,59
60



rd = {}
fc = 0

1. tempNum = 60 - 60%60 -> 60 -0 = 60

rd {60: 1}

2. tempNum =  60 -> 60
final count = 1

rd = {60: 2}

3. tempNum = 60
final = 3

referenceD = {60:3}




'''
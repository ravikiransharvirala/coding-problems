"""
[1,5,10, 100]

Eg 38

while n != 0:
-1
-2
-3
-4


[1,5, 10, 100]

38

while target != 0

38 - 100 >  0
count = 

"""




def solution(denom, target):
    count = 0
    idx = -1
    while target != 0 and idx >= -len(denom):
        if target - denom[idx] > 0:
            target =  target - denom[idx]
            count += 1
        else:
            idx = -1+idx
    return count

denom = [1,5,10,100]
target = 38
print(solution(denom, target))

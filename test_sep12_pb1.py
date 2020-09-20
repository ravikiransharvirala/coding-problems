"""



You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version



versions = [1, 2, 3, 4, 5, 6]

if isBadversion(False)

version_truth = [1, 1, 1, 0, 0, 0, 0]


6

6/3
4:

"""

def isBadVersion(n):
    version_truth = [0, 0, 0, 0, 1, 1, 1]
    if version_truth[n] == 0:
        return False
    else:
        return True

def solution(nversions):
    start = 1
    end = nversions
    while start < end:
        mid = start+(end-start)//2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid+1
    return start

print(solution(7))

"""
[1,None,1,2,None] --> [1,1,1,2,2]
"""

def noneinplace(arr):
    #new_arr = []
    for i in range(len(arr)):
        if arr[i] == None:
            #new_arr.insert(i, arr[i-1])
            arr.insert(i, arr[i-1])
            arr.pop(i+1)
    return arr


arr = [1,None,1,2,None]
print(noneinplace(arr))
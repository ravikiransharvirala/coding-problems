"""
lists = [[[1, 2, 3], [4, 5]], [6, 7, 8]]
"""

def flatten(lists):
    if len(lists) == 1:
        if isinstance(lists[0], list):
            result = flatten(lists[0])
        else:
            result = lists
    elif isinstance(lists[0], list):
        result = flatten(lists[0]) + flatten(lists[1:])
    else:
        result = [lists[0]] + flatten(lists[1:])
    return result


lists = [[[1, 2, 3], [4, 5]], [6, 7, 8]]

print(list(flatten(lists)))
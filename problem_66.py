# Problem 66: Find intersection of two lists
# Find and fix the error

def intersection(list1, list2):
    set2 = set(list2)      # fast lookup
    result = []
    for item in list1:
        if item in set2:
            result.append(item)
    return result

l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
print(f"Intersection: {intersection(l1, l2)}")


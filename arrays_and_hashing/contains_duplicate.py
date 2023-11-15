def contains_duplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)
    return False

a = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(contains_duplicate(a))
print(contains_duplicate(b))
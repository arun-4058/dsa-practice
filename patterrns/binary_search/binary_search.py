# most generalized binary search

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)
    while left < right:
        mid = left + (right-left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left
def quicksort(lists: list):
    if len(lists) < 2:
        return(lists)
    else:
        mid = lists[0]
        less = [s for s in lists[1:] if s < mid]
        more = [s for s in lists[1:] if s > mid]
    return(quicksort(less) + [mid] + quicksort(more))

a = [13, 13, 2, 3, 50, 43, 89, 15, 100]
print(quicksort(a))
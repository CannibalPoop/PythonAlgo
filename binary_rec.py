def binary_rec(list, low, high, ans):
    mid = (low + high) // 2
    if list[mid] == ans:
        return mid
    elif low >= high:
        return(None)
    elif list[mid] <= ans:
        low = mid + 1
        mid = binary_rec(list, low, high, ans)
    elif list[mid] >= ans:
        high = mid - 1
        mid = binary_rec(list, low, high, ans)
    return(mid)

a = [1, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19]
b = 100
l = 0
h = len(a) - 1
print('searched index = ', binary_rec(a, l, h, b))
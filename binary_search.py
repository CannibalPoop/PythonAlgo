def bins(list, ans):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == ans:
            return(mid)
        if guess < ans:
            low = mid + 1
        if guess > ans:
            high = mid - 1
    return(None)
a = [1, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19]
n = 8
print(bins(a, n))
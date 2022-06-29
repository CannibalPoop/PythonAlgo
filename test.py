def sort(list):
    for j in range(len(list)):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return(list)

a = [2, 1, 13, 14, 63, 4, 8, 3, 15, 9]
print(sort(a))
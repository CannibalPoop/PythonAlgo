def sum(list):
    if len(list) == 1:
        return(list[0])
    else:
        a = list[0]
        list.pop(0)
        ans = a + sum(list)
    return(ans)
a = [int(i) for i in range(1000)]
print(sum(a))
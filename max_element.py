def max_element(maximum, list):
    if len(list) == 0:
        return(maximum)
    if maximum <= list[0]:
        maximum = list[0]
    list.pop(0)
    maximum = max_element(maximum, list)
    return(maximum)
a = [11, 12, 3, 132, 15, 2, 192, 168, 1, 87]
m = a[0]
n = max_element(m, a)
print('maximum element = ', n)


def partion(l, low, high):
    x = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= x:
            i += 1
            l[i], l[j] = l[j], l[i]

    l[i + 1], l[high] = l[high], l[i + 1]
    return (i + 1)


def quicksort(l, low, high):
    if low < high:
        r = partion(l, low, high)
        quicksort(l, low, r - 1)
        quicksort(l, r + 1, high)


l = [12, 34, 5, 4, 3, 3, 3, 2, 5, 7, 90, 3, 52, 145]

n = len(l)
quicksort(l, 0, n - 1)
for ik in range(len(l)):
    print(l[ik])

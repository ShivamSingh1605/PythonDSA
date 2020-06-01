a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 0
h = len(a) - 1


def binarysearch(a, l, h, x):
    if l > h:
        return -1
    mid = int(l + (h - l) / 2)
    if(a[mid] == x):
        return mid
    elif a[mid] > x:
        return binarysearch(a, l, mid - 1, x)
    else:
        return binarysearch(a, mid + 1, h, x)


y = binarysearch(a, l, h, 5)
print(y)

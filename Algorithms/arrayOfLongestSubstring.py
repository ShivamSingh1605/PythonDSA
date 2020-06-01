strings = "aaaaaaaaaa"
j = 0
lps = []
lps.append(0)
i = 1
while(i < len(strings)):
    if strings[j] == strings[i]:
        lps.insert(i, j + 1)
        i += 1
        j += 1
    else:
        if j != 0:
            j = lps[j - 1]
        else:
            lps.insert(i, 0)
            i += 1
print(lps)

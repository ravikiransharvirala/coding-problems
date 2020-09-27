def sockMerchant(ar):
    count_color = {}
    for s in ar:
        count_color[s] = count_color.get(s, 0) + 1
    pairs = 0
    for v in count_color.values():
        temp = v
        while temp > 1:
            if temp%2 == 0:
                temp = temp-2
                pairs += 1
            else:
                temp = temp -1
    return pairs

ar = "4 5 5 5 6 6 4 1 4 4 3 6 6 3 6 1 4 5 5 5"
ar = ar.split(" ")
print(sockMerchant(ar))
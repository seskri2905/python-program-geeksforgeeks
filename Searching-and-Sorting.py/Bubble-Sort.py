def bubbleSort(list_a):
    for i in range(0,len(list_a)):
        swapped = False
        for j in range(0,len(list_a) - i - 1):
            if list_a[j] > list_a[j + 1]:
                list_a[j],list_a[j + 1] = list_a[j + 1], list_a[j]
                swapped = True

        if not swapped:
            break

    return list_a

print(bubbleSort([87,0,61,-6]))
        
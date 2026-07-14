def selectionSort(list_a):
    indexing_length = range(0,len(list_a)-1)

    for i in indexing_length:
        min_value = i
        for j in range(i+1,len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a

print(selectionSort([3,9,1,2,63,0]))

""" 
Time Complexity: O(N^2)
Space complexity = 0(1) 
"""
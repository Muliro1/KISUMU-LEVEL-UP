def find_smallest(alist):
#time complexity is O(n * n)
    smallest = alist[0]

    smallest_index = 0

    for i in range(1, len(alist)):

        if alist[i] < smallest:

            smallest = alist[i]

            smallest_index = i
            
    return smallest_index

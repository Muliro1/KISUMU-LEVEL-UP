#recursive sum of a list

def summer(arr):
    counter = 0
    if len(arr) == 1:
        return arr[0]
    for i in range(1, len(arr + 1)):
        counter = arr[0] + summer(arr[i + 1])

    return counter
        

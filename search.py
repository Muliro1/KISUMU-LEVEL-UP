

def binary_search(Item, alist):

	if not isinstance(alist, list):

		raise TypeError('second input must be a list')

	found = False

	bottom = 0

	top = len(alist)- 1

	while bottom <= top and not found:

		middle = (bottom + top) // 2

		if alist[middle] == Item:

			found = True

		elif alist[middle] < Item:

			bottom = middle + 1

		else:

			top = middle - 1
	print(found)

	return found

binary_search(0, [0,1,2,3,4,5,6])

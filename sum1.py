def addition(num1, num2):
	'''
	This function takes in two integer arguments and returns the sum
	'''
	if not isinstance(num1, int) or not isinstance(num2, int):
		return('both arguments must be integers')
	try:
		return num1 + num2
	except:
		print('An Error has occurred')


sum(1,3)
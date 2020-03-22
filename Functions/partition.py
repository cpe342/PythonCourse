def partition(list,func):
	return [[n for n in list if func(n)],[n for n in list if not func(n)]]
	

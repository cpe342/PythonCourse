def triple_and_filter(li):
	return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, li)))
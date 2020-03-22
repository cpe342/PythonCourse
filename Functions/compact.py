def compact(list):
	return [n for n in list if n]
	

print(compact([0,1,2,"",[], False, {}, None, "All done"]))


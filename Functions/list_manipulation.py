def list_manipulation(list,comm,location,value=None):
	if(comm=="remove"):
		if(location=="beginning"):
			return list.pop(0)
		elif(location=="end"):
			return list.pop()
	if(comm=="add"):
		if(location=="beginning"):
			list.insert(0,value)
			return list
		elif(location=="end"):
			list.append(value)
			return list

list_manipulation([1,2,3,4],"remove","beginning",0)
def is_palindrome(string):
	string=str(string).replace(" ","")
	rev=string[::-1]
	if(rev==string):
		return True
	else:
		return False
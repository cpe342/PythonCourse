def multiply_even_numbers(list):
	mult=1;
	for n in list:
		if n%2==0:
			mult*=n
	return mult


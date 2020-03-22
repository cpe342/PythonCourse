def multiple_letter_count(string):
	return {let:string.count(let) for let in string}
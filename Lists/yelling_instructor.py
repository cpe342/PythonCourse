instructor={
	'name':'Canyon',
	'city':'Austin',
	'color':'blue'
}

print(instructor)

yellings_instructor= {key.upper():value.upper() for key,value in instructor.items()}

print(yellings_instructor)
def speak(ani="dog"):
	if(ani=="pig"):
		return "oink"
	elif(ani=="duck"):
		return "quack"
	elif(ani=="cat"):
		return "meow"
	elif(ani=="dog"):
		return "woof"
	else:
		return "?"

print(speak())
print(speak("cat"))
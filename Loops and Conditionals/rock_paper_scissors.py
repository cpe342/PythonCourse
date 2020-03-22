from random import choice

play=input("(Enter your choice): ")
com_play=choice(["rock","paper","scissors"])

print(f"Player chose {play}")
print(f"Computer chose {com_play}")

if(play==com_play):
	print("Tie!")

elif play=="rock":
	if com_play=="paper":
		print("Computer wins")
	elif com_play =="scissors":
		print("Player wins")

elif play=="paper":
	if com_play=="scissors":
		print("Computer wins")
	elif com_play =="rock":
		print("Player wins")

elif play=="scissors":
	if com_play=="rock":
		print("Computer wins")
	elif com_play =="paper":
		print("Player wins")
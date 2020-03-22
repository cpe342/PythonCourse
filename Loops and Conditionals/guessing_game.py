from random import randint

play="y"
while(play!="n"):
	num=randint(1,10)
	print("Guess a number from 1-10")
	guess=int(input())
	if(guess==num):
		print("You win!")
		break
	else:
		print("You're wrong")
	play=input("Keep playing? (y/n)")

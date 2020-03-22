num1=[1,2,3,4] 
num2=[3,4,5,6]
answer=[]

answer=[n for n in num1 if n in num2]
print(list(answer))

names=["Ellie","Tim","Matt"]
answer2=[n[::-1].lower() for n in names]
print(list(answer2))
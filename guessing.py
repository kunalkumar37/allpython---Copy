import random 
n=20
to_be_guessed=int(n*random.random())+1     # here in this line there is a generation of 
#from 1 to 20

guess=20
while guess != to_be_guessed:
    guess=int(input("new nummber"))

    if 
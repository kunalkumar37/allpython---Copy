travelling=input("yes or no\n")
while travelling =="yes":
    num=int(input("number of people travelling\n"))

    for num in range(1,num+1):
        name=input("name::")

        age=input("age::")

        sex=input("male or feamale")
        print(name)
        print(age)
        print(sex)
    print("yes or no if u forget something\n")
    travelling=input("opps forgot someone")
 
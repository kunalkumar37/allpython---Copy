print("welcome ot iron bank of naula")
restart=('y')
chances=3
balance=16000
while chances>=0:
    pin=int(input("wnter the 4 digit pin::"))
    if pin==(1234):
        print("u have entered the in correctly")
        while restart not in ('n','no','NO','N'):
            print("pleasae press 1 for your balance\n:")
            print("please press 2 to make the withdrawl\n:")
            print("please press 3 to pay::\n")
            print("please press 4 to return card\n:")
            option=int(input("what would u like to enter?"))
            if option==1:
                print("your balance is :",balance,"\n")
                restart=input("would u like to go back??")
                if restart in ('n','no','NO','N'):
                    print("thank u")
                    break
            elif option==2:
                option2='y'
                withdrawl=float(input("how much would u like to withdraw"))
                if withdrawl>=500:
                    balance=balance-withdrawl
                restart=input("would u like to go back\n")
                if restart in ('n','no','NO','N'):
                    print("thank u")
                    break
            elif option=3:
                payin=float(input("enter the amount ot pay\n"))
                balance=balance+payin
                print("ur balance is::",balance)

                restart=input('n','no','NO','N')
                if restart in ('n','no','NO','N'):
                    print("thanku for paying ::\n")
                    break;
            elif option==4:
                print("please wait whilst ur card is returned \n")
                print("thanku for ur service\n")
                break
            else:
                print("please enter a correct number\n")
                restart=('y')

    else:
        print("incorrect password")
        chances=chances-1
        if chances==0:
            print("no more tries left::\n")
            break



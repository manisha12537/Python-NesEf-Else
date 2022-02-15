print("welcome to my ATM")
card=input("enter your card ")
if card=="insert":
    print("insert succesfull")
    language=input("select any language")
    if language=="inglish" or language=="hindi" or language=="marathi":
        print("show information from this language")
        pin=int(input("eneter your card pin number"))
        if pin<=50000:
            print("password is corect")
            acount=input("kis type ka transioncion krna chahte ho")
            if acount=="curent" or acount=="seving":
                print("being prosess")
                mony=int(input("enter the amount"))
                if mony<=20000:
                    print("sucssesful withdraw")
                else:
                    print("etna withdraw nhi kar sakte")
            else:
                print("not being prosses")
        else:
            print("password is wrong")
    else:
        print("language not sapported")
else:
    print("try again")
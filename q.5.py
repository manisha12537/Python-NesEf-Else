print("WELCOME TO FACEBOOK")
name=input("eneter your name")
if name>"a" and name<"z":
    print("its your name")
    age=int(input("enter your age"))
    if age>18:
        print("your age age safisiant for use facebook")
        print("your age is difind")
        otp=input("eneter the otp")
        if otp<="9999":
            print("otp is correct")
            login=input("eneter click the login")
            if login=="yes":
                print("login succsfull")
                print("facebook is open")
            else:
                print("login is unsuccesfull")
        else:
            print("please eneter the correct otp")
    else:
        print("age is not difind")
else:
    print("name is not difinde")

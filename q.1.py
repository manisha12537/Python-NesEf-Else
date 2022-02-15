day=input("enter the day wich day you went outside in campus")
if day=="monday":
    print("outside ja skte hai")
    permission=input("disco ne permision di ya nhi no/yes")
    if permission=="yes":
        print("permission mil gai hai,aap ja skte ho")
        time=input("kis time pe return aaye ho outside se")
        if time <="6":
            print("campus me entry milegi")
            work=input("kis kam ke bahar gaye ho ")
            if work=="NGwork":
                print("quarantine nhi hoge")
            else:
                print("quarantine hoge")
        else:
            print("campus me entry nhi milegi")
    else:
        print("bahar nhi ja skte")
else:
    print("bahar nhi ja skte")


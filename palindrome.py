
v=int(input("enter a value:"))

if(v>=0):
    if((v>=100) and (v<=999)):
        a=v//10
        b=v%10
        c=a//10
        d=a%10
        e=(b*100)+(d*10)+(c*1)
        print(e)
        if(v==e):
            print("\nPALINDROME")
        else:
            print("\nNOT PALINDROME")
    else:
        print("INVALID")
else:
    print("-ve not allowed")
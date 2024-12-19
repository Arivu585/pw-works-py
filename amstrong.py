print("\nAMSTRONG NUMBER")

v=int(input("\nEnter a three digit value:"))

if(v>=0):
    if((v>=100) and (v<=999)):
        a=v//10;
        b=v%10;
        c=a//10;
        d=a%10;
        e=(c*c*c)+(d*d*d)+(b*b*b)
        if(v==e):
            print("\nAMSTRONG NUMBER")
        else:
            print("\nNOT A AMSTRONG NUMBER")
    else:
        print("\nvalue not allowed")
else:
    print("\n-ve value not allowed")

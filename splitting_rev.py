v=int(input("\nEnter a three digit value:"))

if((v>=100) and (v<=999)):
    a=v//10
    b=v%10
    c=a//10
    d=a%10
    print("1's is :",b)
    print("10's is :",d)
    print("100's is :",c)
    e=(b*100)+(d*10)+(c*1)
    print("\nReversed value is",e)
else:
	print("\nvalue not allowed")

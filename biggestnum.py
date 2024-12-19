a=int(input("VALUE OF A:"))
b=int(input("VALUE OF B:"))
c=int(input("VALUE OF C:"))

if((a>b) and (a>c)):    #10>5 and 10>3
    print("A is BIGGEST")
    
elif((b>a) and (b>c)):  #10>5 and 10>5
    print("B is BIGGEST")

elif((c>a) and (c>b)):  #10>5 and 10>3
    print("C is BIGGEST")
    
elif((a==b) and (a>c)):
    print("A and B are Equal, C is SMALLEST")
    
elif((a==c) and (a>b)):
    print("A and C are Equal, B is SMALLEST")

elif((b==c) and (b>a)):
    print("B and C are Equal, A is SMALLEST")
else:
    print("ALL ARE EQUAL")
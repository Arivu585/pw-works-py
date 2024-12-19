print("PRINT DIGIT")

v=int(input("\nEnter a number:"))

if((v>=0) and (v<=9)):
    if(v==0):
        print("ZERO")
    elif(v==1):
        print("ONE")
    elif(v==2):
        print("TWO")
    elif(v==3):
        print("THREE")
    elif(v==4):
        print("FOUR")
    elif(v==5):
        print("FIVE")
    elif(v==6):
        print("SIX")
    elif(v==7):
        print("SEVEN")
    elif(v==8):
        print("EIGHT")
    elif(v==9):
        print("NINE")
    else:
        print("ONLY 0 TO 9 MUST")
else:
    print("INVALID")
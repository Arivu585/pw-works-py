print("\nSWAPPING without Temporary variable")

a=int(input("\nEnter the value of A:"))
b=int(input("\nEnter the value of B:"))

a=a+b
b=a-b
a=a-b

print("SWAPPED")

print("\nA is",a)
print("\nB is",b)
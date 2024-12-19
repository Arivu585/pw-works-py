s=int(input("Enter the Start:"))
e=int(input("Enter the end:"))
while s<=e:
	n=s%100
	if n%2==0:
		print(s)
	s+=1
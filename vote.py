age=int(input("\nEnter your age:"))

if(age>0):
	if(age>=18):
		print("\nEligible for vote")
	else:
		print("\nNOT Eligible for vote")
else:
	print("\n-ve values not allowed")
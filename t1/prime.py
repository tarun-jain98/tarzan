val = int(input("Enter no. to check for prime: "))
if isPrime(val):
	print(val+" is a prime number")
else:
	print(val+" is not a prime number")


def isPrime(num):
	for i in range(2,num-1):
		if num % i == 0:
			return False

	return True

		

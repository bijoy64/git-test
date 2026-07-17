def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2,n):
            if (n%i==0):
                return False
        return True
prime = int(input("Enter a number: "))
if (test_prime(prime))==False:
    print(prime, "is not a prime number")
else:
    print(prime, "is a prime number")
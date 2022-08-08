# Name: Sylvester Kojo Mintah
# Student ID: 10972004

n = int(input("Enter a number: "))

sum = 0
for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i, "is prime")
        sum += i
print("Therefore the sum of prime numbers is " + str(sum))
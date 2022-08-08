# Name: Sylvester Kojo Mintah
# Student ID: 10972004

sum = 0;
count = 0
for i in range (10001):
    if i % 2 == 0:
        sum += i
        count += 1
print("The sum of all even numbers from 0 to 10000 is " + str(sum))
print("The number of even numbers fron 0 to 10000 is " + str(count))

average = sum / count;
print("Therefore the average of even numbers from 0 to 10000 is " + str(average))
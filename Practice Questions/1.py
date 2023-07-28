num = int(input("How Many numbers you want to enter? "))
sum =0
for i in range(num):
    numbers = float(input("Enter any number: "))
    sum = sum + numbers

avg = sum/num
print("The Average of Numbers is: ", avg)   
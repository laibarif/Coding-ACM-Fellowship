import time
start_time = time.time()
def sumFunction():
    n = int(input("Enter any number: "))
    sum =0
    for i in range(n):
        sum = sum+(n-i)
    end_time = time.time()
    return sum,end_time-start_time

print(sumFunction())
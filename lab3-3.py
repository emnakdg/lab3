user = input("Write numbers (example : 1,2,2,5): ")
numbers = user.split(",")

try:
    for number in numbers:
        numbers[numbers.index(number)] = int(number)

    my_set = set(numbers)
    print(my_set)
    
except:
    print("bad data")
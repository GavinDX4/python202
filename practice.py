
for first_num in range(1, 100):
    if first_num % 5 == 0 and first_num % 3 == 0:
        print("FizzBuzz")
    elif first_num % 3 == 0:
        print("Fizz")
    elif first_num % 5 == 0: 
        print("Buzz")
    else:
        print(first_num)
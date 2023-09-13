# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

print(fizbuzz(5))

list = ["Chicken", "Hydrolic Press", "Lebron James", "Gynocolgist", "Dark Matter"]
print(list)
#print(list.reverse())
print(list[1:4])


def add_two(n):
    m = n + 2
    print(m)
    return m

"""assert add_two(5) == 7 
assert add_two(-2) == 0 
assert add_two(0) == 2"""

y = add_two(2)

def factorial(n: int) -> int:

    result = 1
    for x in range(1,n + 1):
        result = result * x
    return result

print(factorial(4))
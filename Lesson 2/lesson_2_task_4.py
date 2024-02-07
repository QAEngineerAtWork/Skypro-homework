'''FizzBuzz. Задачка с собеседования'''

def fizz_buzz(n:int):
    for x in range(1, n):    #лучше написать n+1 именно здесь, а не n=21 внизу
        if (x % 4 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        else:
            if (x % 5 == 0):
                print("Buzz")
            else:
                if (x % 4 == 0):
                    print("Fizz")
                else:
                    print(x)

n = 21
fizz_buzz(n)
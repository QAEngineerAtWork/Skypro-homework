'''Високосный год'''

def is_year_leap(n:int):
    
    if (n % 4 == 0):
        return True
    else :
        return False    

year = 2024

result = is_year_leap(year)
print("год " +str(year) + ": " +str(result))

# print(f"год {year}: {result}")
# print("год {}: {}".format(year, result))


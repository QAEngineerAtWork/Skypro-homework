'''Месяц — сезон.Написать функцию, которая принимает номер месяца и возвращает название сезона, к которому относится этот месяц'''

def month_to_season(number:int):
    if number in (1, 2, 12):
        print("Зима")
    elif number in (3, 4, 5):
        print("Весна")
    elif number in (6, 7, 8):
        print("Лето")
    elif number in (9, 10,11):
        print("Осень")
    else:
        print("Некорректный ввод")

number = 13

month_to_season(number)
                


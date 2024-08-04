from smartphone import Smartphone 

phone1 = Smartphone("Apple", "iPhone 12", "+79991111111")
phone2 = Smartphone("Samsung", "Galaxy S21", "+79992222222")
phone3 = Smartphone("Xiaomi", "Mi 11", "+79993333333")
phone4 = Smartphone("HONOR", "X8A", "+79994444444")
phone5 = Smartphone("HUAWEI", "11i", "+79995555555")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")

from address import Address 
from mailing import Mailing


to_address = Address(420000, "город Казань", "улица Ленина", 3, 150)
from_address = Address(167000, "город Сыктывкар", "улица Гоголя", 18, 67)

mailing = Mailing(to_address, from_address, 780, 16700012345678)

print(f"Отправление {mailing.track} из {mailing.from_address.zip_code}, {mailing.from_address.city}, {mailing.from_address.street}, дом {mailing.from_address.house}, квартира {mailing.from_address.flat}\
 в {mailing.to_address.zip_code}, {mailing.to_address.city}, {mailing.to_address.street}, дом {mailing.to_address.house}, квартира {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")

from src.widget import get_date
from src.widget import mask_account_card

print(mask_account_card("Счет 12345678901234567890"))
print(mask_account_card("Visa Classic 1234567890123456"))
print(f"Дата: {get_date("2024-03-11T02:26:18.671407")}")

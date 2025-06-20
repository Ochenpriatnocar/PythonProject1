from src.masks import get_mask_account
from src.masks import get_mask_card_number

print(f"Номер счета карты: {get_mask_account("12345678901234567890")}")
print(f"Номер карты: {get_mask_card_number("1234567890123456")}")

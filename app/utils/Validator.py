import re

def PhoneNumberValidator(numberi: str) -> str:
    number = numberi.strip()
    lenNumber = len(number)
    numberCheck = f'\d\d\d\d\d\d\d\d\d\d\d'
    numberCheckd = f'\d\d\d-\d\d\d\d-\d\d\d\d'
 
    ck = not(re.findall(numberCheck, number)) == bool(re.findall(numberCheckd, number))\
        and 11 == lenNumber or lenNumber == 13 and number[:3] == "010"
    if not ck:
        raise TypeError("Invalid phone number")
    else:
        if lenNumber == 13:
            return number.replace("-", "")
        return number
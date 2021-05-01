def count_char(string: str) -> dict:
    capital = 0
    small = 0
    number = 0
    other = 0
    for char in string:
        if "A" <= char <= "Z":
            capital += 1
        elif "a" <= char <= "z":
            small += 1
        elif "0" <= char <= "9":
            number += 1
        else:
            other += 1
    return {'capital letter': capital, 'small letter': small,
            'number': number, 'other character': other}


text = 'nfd av 32 JF fsgsa'
print(count_char(text))

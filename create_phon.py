def create_phone_number(numeros):
    
    return f'({numeros[0]}{numeros[1]}{numeros[2]}) {numeros[3]}{numeros[4]}{numeros[5]}-{numeros[6]}{numeros[7]}{numeros[8]}{numeros[9]}'

if __name__ in '__main__':
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
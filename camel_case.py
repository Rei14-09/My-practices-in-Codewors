def to_camel_case(text):
    new_text = ''
    mayuscula = False

    for letra in text:
        if letra.isalpha():
            if mayuscula:
                new_text += letra.upper()
                mayuscula = False
            else:
                new_text += letra
        else:
            mayuscula = True

    return new_text

if __name__ in '__main__':
            assert to_camel_case("") == ""
            assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
            assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
            assert to_camel_case("A-B-C") == "ABC"
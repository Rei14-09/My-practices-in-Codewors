def get_middle(string):
    
    if len(string)%2 == 0:
        mitad_par = len(string) // 2 #Refactorizable con una función que haga la mitad
        return string[mitad_par-1 : mitad_par+1]
        
    elif len(string) == 1:
        return string
    
    else:
        mitad_impar = len(string) // 2
        return string[mitad_impar]

if __name__ in '__mine__':
        assert get_middle("test") == "es"
        assert get_middle("testing") =="t"
        assert get_middle("middle") == "dd"
        assert get_middle("A") == "A"
        assert get_middle("of") == "of"
def freq_seq(s, sep):
    
    resultado = []
    
    for caracter in s:
        tirada = str(s.count(caracter))
        resultado.append(tirada)
        
    return  sep.join(resultado)

if __name__ in '__main__':
        assert freq_seq('hello world', '-') == '1-1-3-3-2-1-1-2-1-3-1'
        assert freq_seq('19999999',    ':') == '1:7:7:7:7:7:7:7'
        assert freq_seq('^^^**$',      'x') == '3x3x3x2x2x1'
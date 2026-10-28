def money_change(money):

    try:

        assert isinstance(money,int)

        list_coins = [5, 2, 1]
        change = []
        for coin in list_coins:
            change.append(money // coin)
            money %= coin

        assert not money

        return tuple(change)
    except:
        return None

if __name__ in '__main__':
    assert money_change(8) == (1,1,1)
    # >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
    assert money_change(5) == (1,0,0)
    # >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
    assert money_change(29) == (5,2,0)
    # >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
    assert money_change(0) == (0,0,0)
    # >>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
    assert money_change(170) == (34,0,0)
    # >>> (34, 0, 0)  # treinta y cuatro de 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
    assert money_change(267) == (53,1,0)
    # >>> (53, 1, 0)  # cincuenta y tres de 5 cénts, una de 2 cénts y ninguna de 1 cént.
    assert money_change(-2) == None
    # >>> None
    assert money_change(5.576) == None
    # >>> None
    assert money_change("5") == None
    # >>> None
    assert money_change([2,2,2]) == None
    # >>> None
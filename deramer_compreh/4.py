def bag(dct, cash):
"""принимет список товаров и кэш, сравнивает значения под ключами со средствами,
записывает в новый массив то, что можно купить, выводит его"""
    result = []
    for key in dct:
        if int(dct[key]) <= int(cash):
            result.append(key)
    print(result)


dct = {'karasevnik': '2000', 'fisos 10000 brs': '1', 'matan 0 brs': '5', 'analit 10 brs': '10'}
cash = '5'
bag(dct, cash)

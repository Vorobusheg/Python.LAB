def bag(dct, cash):
    result = []
    for key in dct:
        if int(dct[key]) <= int(cash):
            result.append(key)
    print(result)


dct = {'karas' : '20', 'fiso' : '1', 'matan' : '5', 'anal' : '10'}
cash = '5'
bag(dct, cash)

from operator import itemgetter

def fruit_input(fruitlist):
    print('--------------현재 재고현황---------------')
    for i in fruitlist:
        print(i['fruit'], i['price'], i['stock'])
    print('------------------------------------------')
    fruitl = {'fruit' : '', 'price' : '', 'stock' : ''}
    while True:
        fruitl['fruit'] = input('추가할 과일명을 입력하세요. >>> ')
        check = 0
        for i in fruitlist:
            if i['fruit'] == fruitl['fruit']:
                check = 1
                break
        if check == 0:
            break
        print('중복되는 과일이 존재합니다.')
    price = 'a'
    while not fruitl['price'].isdecimal():
        price = input('추가할 메뉴의 가격을 입력하세요. >>> ')
        break
    fruitl['price']=int(price)
    number = 'b'
    while not fruitl['stock'].isdecimal():
        stock = input('추가할 메뉴의 수량을 입력하세요. >>> ')
        break
    fruitl['stock']=int(stock)
    fruitlist.append(fruitl)
    print('--------------추가된 재고현황---------------')
    for i in fruitlist:
        print(i['fruit'], i['price'], i['stock'])
    print('--------------------------------------------')
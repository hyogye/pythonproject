# 과일가게 재고 프로그램
# - 1.입력 : 딕셔너리{과일명, 가격, 재고}, 과일 추가
# - 2.판매 : 데이터를 입력받아서 남은 재고 출력
# - 3.재고리스트 : 재고 내림차순 정렬 후 출력
# - 4.삭제 : 재고가 0이면 재고가 없다는 메세지 출력 후 남은 재고리스트 출력
# - 5.종료 : 프로그램 종료
# 단점 - 계속 마이너스가 된다는 점 

import json

fruitlist = [{'fruit': '수박', 'price': '8000', 'stock' : 5},
            {'fruit': '청포도', 'price': '7000', 'stock' : 6},
            {'fruit': '딸기', 'price': '7500', 'stock' : 10}]
while True:
    choice = input('''1.입력 2.판매 3.재고리스트 4.삭제 5.종료
번호를 선택하세요 >>> ''')
    
    if choice == '1':
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

    elif choice == '2':
        print('--------------현재 재고현황---------------')
        for i in fruitlist:
            print(i['fruit'], i['price'], i['stock'])
        print('--------------------------------------------')

        while True:
            choice1 = input('판매한 과일을 입력하세요. :')
            idx = -1
            for i in range(len(fruitlist)):
                if fruitlist[i]['fruit'] == choice1:
                    idx = i
                    break
            if idx == -1:
                print('등록되어있지 않은 과일입니다.')
                break
            choice2 = input('판매한 수량을 입력하세요. : ')
            stock2 = int(fruitlist[i]['stock'])
            stock2 -= int(choice2)
            if stock2 < 0:
                s = fruitlist[i]['stock']
                print('재고가 없습니다')
            else:
                fruitlist[i]['stock']=stock2
            break
            # sale = fruitlist[idx]['stock']-int(choice2)
            # print(f'{choice1}을 {choice2}개를 판매하여 {sale}개가 남았습니다.')
            # fruitlist[idx]['stock'] = sale
            # if fruitlist[idx]['stock'] <= 0:
            #     print("재고가 없습니다.")
         
            # if choice2 == 'q':
            #     break
            # print('----------------------------------------')
            # for i in fruitlist:
            #     print(i['fruit'], i['price'], i['stock'])
            # print('----------------------------------------')
            
    elif choice == '3':
        print('---------------재고 리스트---------------')
        for i in fruitlist:
            print(i['fruit'], i['price'], i['stock'])
        print('-----------------------------------------')

# 부족한 점
    elif choice == '4':
        for idx in range(len(fruitlist)):
            if fruitlist[idx]['stock'] == 0:
                print('재고x : ', fruitlist[idx])

            elif fruitlist[idx]['stock'] != 0:
                print('재고o : ', fruitlist[idx])

    elif choice == '5':
        print('프로그램을 종료합니다')
        f = open('fruit_store.json','w')
        json.dump(fruitlist,f)
        f.close()  
        break

    else:
        print('메뉴를 잘못 선택하셨습니다.')

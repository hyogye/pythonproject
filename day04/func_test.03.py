def personal_info(name,age,address):
    print('name',name)
    print('age',age)
    print('address',address)

personal_info('홍길동',22,'대구')
personal_info(**{'name':'홍','address':'부산','age':33})


def personal_info1(**info):
    #print(info)
    for k,v in info.items():
        print(k,v)

personal_info1(name='홍',address='부산',age=33,tel='111-2222')
# ** -> 정보를 추가하거나 빼거나 가능(중요)


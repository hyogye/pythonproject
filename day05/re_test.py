import re

from day05.function_customer import customer__n

# a = 'hello, world'
# print(re.match('world',a))

# print(re.search('^world',a))

# print(re.search('world$',a))       전체주석처리는 ctrl + /


# str1 = '123 hello 678 HELLO'
# print(re.match('[0-9]+',str1))
# print(re.match('[0-9]*',str1))
# print(re.search('[0-9]*',str1))

# print(re.match('a*b','ab'))
# print(re.match('a+b','b'))

# print(re.search('^[0-9]{2,3}-[0-9]{4}-[0-9]{4}$','022-3412-5643 tel '))

# p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
# print(p.search('ss7up@gmail.com'))

p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
email = ''
while not p.search(email):
    email = input('email >>>')


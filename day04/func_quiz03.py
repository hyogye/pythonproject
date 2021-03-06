#quiz.03>
#커피메뉴 관리프로그램
#데이터 저장은 딕셔너리로.. {'메뉴명':가격,'coffe':2000}
#프로그램에서 사용할 메뉴
# 1.메뉴입력 2.메뉴수정 3.메뉴목록 4.메뉴삭제 5.프로그램 종료
# - 메뉴입력: 메뉴명과 가격을 입력받아서 저장
# - 메뉴수정: 메뉴명을 확인하고 있는 메뉴에 가격을 입력받아 수정
# - 메뉴목록: 저장된 메뉴명과 가격을 출력(천단위 구분 기호표기), 메뉴명 순서대로 출력
# - 메뉴삭제: 메뉴명을 확인하고 있는 메뉴에서 삭제
# - 프로그램 종료: 프로그램을 종료하는 메시지를 출력하고 종료
# - 메뉴1~5까지만 입력받고 다른 값이 들어오면 관련 에러 메시지를 출력한다
# - 가격은 숫자로 입력해야 된다


import func_basic as fb
menu = {'아메리카노':3000,'달고나라떼':4000,'초코라떼':4500,'석류에이드':3500,'히비스커스':3800}
while True:
    choic = input(''' 
------------------------------------------------------------
 1.메뉴입력 2.메뉴수정 3.메뉴목록 4.메뉴삭제 5.프로그램 종료
------------------------------------------------------------
메뉴선택 >>> ''')
    if choic == '1':
        fb.menu_input(menu)
    elif choic == '2':
        fb.menu_update(menu)
    elif choic == '3':
        fb.menu_list(menu)
    elif choic == '4':
        fb.menu_delete(menu)
    elif choic == '5':
        print('프로그램을 종료합니다.')
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')

# 너무 길 경우 imprt를 사용해서 간단하게 줄일 수 있다 as 뒤에는 요약할 수 있는 단어 넣기
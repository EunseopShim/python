#7
# dict = {'one':1,'two':2,'three':3,'four':4,'five':5}
# a=list(dict.items())
# print(sorted(a))
# print(sorted(a,reverse = True))

#8
# s='one two one two three four'
# s1=s.split()
# a = []
# for i in range(len(s1)):
#     if (s1[i] in a) == True:
#         continue
#     elif (s1[i] in a) ==False:
#         a.append(s1[i])
# print(a)

#9
# price = {'배':(2000,3),'사과':(1500,5),'딸기':(1800,2),'참외':(2300,5)}
# a = list(price.keys())
# k=0; total = 0
# for i in price:
#     if price[i][1] - 5 >=0:
#
#         print('{}는 살 필요가 없습니다.'.format(a[k]))
#     else:
#         print('{}은 사야합니다.'.format(a[k]))
#         print('{}을 사는데 필요한 돈은 {}원 입니다.'.format(a[k],price[i][0] * (5-price[i][1])))
#         total+=price[i][0] * (5-price[i][1])
#     k+=1
# print('총 필요한 돈은 {}입니다.'.format(total))

#10
# tel = {'min':'010-3455-1235','jin':'010-2222-3312','jay':'010-6949-2341','ken':'010-9999-9999','ain':'010-2222-2222'}
# a = input('누구의 번호를 찾을까요 ? --> ')
# if (a in tel) ==True:
#     print(tel.get(a))
# else:
#     print('그런 이름은 없어.')

#11
# idlist = {'가나':1234,"길동":1111,"민수":4321,"수민":2345}
# a = input('ID입력 : ')
# b = input('패스워드 입력 : ')
# if (a in idlist) ==True:
#     if b == str(idlist[a]):
#         print('{}님 가입확인 되었습니다'.format(a))
#     else:
#         print('P/W를 확인하세요')
# else:
#     print('가입이 되어있지 않네요~~')

#12
# dict = {}
#
#
# while True:
#     a = int(input('1.단어등록 , 2.단어찾기 , 3.종료 ==>'))
#     if a ==1:
#         eng = input('영어 : ')
#         kor = input('한글 : ')
#         dict[eng] = kor
#     elif a == 2:
#         need = input('찾고싶은 단어 : ')
#         if (need in dict) == True:
#             print(dict[need])
#         else:
#             print('사전에 단어가 존재하지 않습니다.')
#     elif a == 3:
#         break

#13
# score = {'Prodo':97,'Sally':88,'Neo':70,'Brown':99,'Mini':70}
# print('평균 : {}'.format(sum(score.values())/len(score)))

#14
# a = input('입력 ==> ')
# b = []
# for i in a:
#     if i == 'a':
#         b.append('w')
#     elif i == 'b':
#         b.append( 'x')
#     elif i == 'c':
#         b.append('y')
#     elif i == 'd':
#         b.append( 'z')
#     elif i == 'w':
#         b.append('a')
#     elif i == 'x':
#         b.append( 'b')
#     elif i == 'y':
#         b.append('c')
#     elif i == 'z':
#         b.append('d')
#     else:
#         b.append(i)
#
# k = ''.join(b)
# print(k)

#15
# nation = {'kr':'대한민국','us':'미국','jp': '일본','sk':'슬로바키아','de':'독일','hu':'헝가리', 'no':'노르웨이'}
# for i in nation.items():
#     print(i)

#16
# import random
# problems = {'파이썬':'최근에 가장 떠오르는 프로그래밍 언어','변수':'데이터를 저장하는 메모리 공간','함수':'작업을 수행하는 문장들의 집합에 이름을 붙인것','리스트':'서로관련이 없는 항목들의 모임'}
# a = list(problems.values())
# for i in range(len(a)):
#     print('다음은 어떤 단어에 대한 설명일까요?')
#     q = random.choice(a)
#     print(q)
#     answer = int(input('(1)파이썬 (2)변수 (3)함수 (4)리스트\n정답 : '))
#
#     if a[answer-1] == q:
#         print('정답입니다!')
#     else:
#         print('오답입니다.')

#17

# import collections
# import re
# l = "I love thee with the passion put to use In my old griefs, and with my childhood's faith. " \
#     "I Love thee with a love I seemed to lose" \
#     "With my lost sain t - I love thee with the breath," \
#     "Smiles, tears, of all my life! - and if God choose," \
#     "I shell but love thee better after death."
# a = re.sub('[-,.!\' ]','',l)
# b = collections.Counter(a)
# b1 = list(b.keys())
# b2 = list(b.values())
# print('-'*10)
# print('문자   빈도수')
# print('-'*10)
# for i in range(len(b1)):
#     print('%-5s% -5d' % (b1[i],b2[i]))

#18
# l1 = ['345-4958','334-0948','394-9050','473-3853']
# l2 = ['서울','경기','부산','제주']
# area_no={'서울':'02','경기':'031','부산':'051','제주':'064'}
# a = []
# for i in range(len(l2)):
#     a.append(area_no[l2[i]]+')'+l1[i])
# print(a)






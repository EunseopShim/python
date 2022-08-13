#1
# a = set ()
# print('a=',a)

# b = {1,2,3}
# print('b=',b)

# c = set((1,2,3,1,2,3,1,2,3))
# print('c=',c)
#
# d =set({'one':1,'two':2})
# print(d)

# e = {('spring','summer','fall','winter'),1,2,3,4}
# print(e)

# set_hello = set('hello')
# print(set_hello)

# f = set((1,2,3))
# print(f)

# g = set([1,2,3])
# print(g)



#2
# my_set = {1,2,3}
# print(my_set)
# print(type(my_set))
#
# my_set ={'hello',1.0,(1,2,3)}
# print(my_set)
#
# my_set = {1,2,3,3,4,2}
# print(my_set)
#
# my_set = {}
# print(type(my_set))
# my_set = set()
# print(my_set)
# print(type(my_set))

#3
# color_list = ['red','blue','red','green','pink','blue','black']
# print(color_list)
# color_set = set(color_list)
# print(color_set)

#4
# s_nature = {'sky','sea'}
# print(s_nature)
# print()
#
# s_nature.add('earth')
# s_nature.add('sky')
# print(s_nature)
# print()
#
# print(s_nature.pop())
# print(s_nature)
# print(s_nature.pop())
# print(s_nature.pop())

#5
# s_planet = {'수성','금성','지구','화성','목성','토성','천왕성','해왕성'}
# print(s_planet)
# print()
#
# s_planet.discard('금성')
# print(s_planet)
# s_planet.remove('천왕성')
# print(s_planet)
#
# s_planet.clear()
# print(s_planet)

#6
# A = {1,2,3,4,5,6}
# B = {1,2,3,7,8,9}
#
# print(A|B,'-> A|B')
# print(A.union(B),'-> A.union(B)')
# print(B.union(A),'-> B.union(A)')
# print(A, '-> A')
# print()
#
# print(A & B,'-> A & B')
# print(A.intersection(B),'-> A.intersection(B)')
# print()

# print(A-B, '-> A.difference(B)')
# print(A.difference(B),'-> A.difference(B)')
# print()
#
# print(A^B,'->A^B')
# print(A.symmetric_difference(B),'-> A.symmetric_difference(B)')
# print()
#
# print(A^B,'->A^B')
# print(A.symmetric_difference(B),'-> A.symmmeteric_difference(B)')
# print()
#
# print({4,5,6} <= A)
# print({4,5,6}.issubset(A))
# print({1,2,3,4,5,6} >= A)
# print({1,2,3,4,5,6}.issuperset(A))



#7
# s_float = {1.0,3.0,2.0,10.0}
# print(s_float)
# print()
#
# print(0.0 in s_float)
# print(len(s_float))
# print(max(s_float))
# print(min(s_float))
# print(sum(s_float))
# print(sorted(s_float))
# print(s_float)
# print()
#
# print(set([1,2,3,2,3]))



#HW 1
# fruit_set =set(['딸기','바나나','오렌지','사과'])
# if ('바나나' in fruit_set) == True:
#     print('바나나는 냉장고에 있습니다.')
#
# else:
#     print('바나나는 냉장고에 없습니다.')
# print('냉장고에는 {}개의 과일이 있습니다.'.format(len(fruit_set)))
# fruit_set.discard('바나나')
# print(fruit_set)

#HW 2
# list = set(['홍길동','박상민','강민우','이수지','하누리'])
# late = set(['홍길동','이수지','박상민'])
# absent = set(['박상민','하누리'])
#
# print('보너스를 받을 최고의 사원들 : {}'.format(list-late-absent))
# print('야근을 하게될 불운의 사원들 : {}'.format(late&absent))

#HW 3
# A = {4,3,2,7,8,10,1,9}
# B = {0,1,3,5,6,8,9,10,4}
# print(A in B)
# if (A in B) == False:
#     print(A|B)

#HW 4
# U = {'A','B','C','D','E','F','G','H','I','J','K','L','M'}
# A = {'D','C','L','J','K'}
# B = {'L','B','H','E'}
#
# print(U-(A|B))

#HW 5
# a = {'비누':(3,2),'칫솔':(5,4),'샴푸':(2,1),'치약':(4,4),'로션':(5,3)}
# a1 = list(a)
# b = set()
# b1 = set()
# for i in a1:
#     if a[i][0] >= 4 and a[i][1] >= 4:
#         b.add(i)
#     elif a[i][0] < 4 and a[i][1] <= 4:
#         b1.add(i)
# print(b)
# if '로션' in b1 == True:
#     print('로션은 판매중지에 해당된다.')
# else:
#     print('로션은 판매중지에 해당 안 됨')

#HW 6
# num2 = set()
# num3 = set()
# for i in range(1,101,1):
#     if i%2 ==0:
#         num2.add(i)
#     if i%3 ==0:
#         num3.add(i)
# print(len(num2|num3))

#HW 7
# num16 = {1,2,4,8,16}
# num30 = {1,2,3,5,6,10,15,30}
# print(num16&num30)

#HW 8
# a,b,c,d,e,f,g,h,i,j = map(int,input('10개의 수 입력 : ').split())
# set = {a,b,c,d,e,f,g,h,i,j}
# print(max(set))

#HW 9
# str1 = 'This is my best'
# str2 ='Do your best'
# a = set(str1.split())
# b = set(str2.split())
# print(a&b)

#HW 10
# a = set()
#
# for i in range(1,101,1):
#     for j in range(1,101,1):
#         for k in range(1,101,1):
#             if i + j + k ==100:
#                 a.add(i)
#
#
# a1 = sorted(list(a))
# print(set(a1))
# print('==> {}개'.format(a1[-1]))




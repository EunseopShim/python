#1
# print(dir(__builtins__))

#2
# a = 10
# print(dir())

#3(1
# import re
# print(dir(re))

#3(2
# b=[1,2,3]
# print(dir(b))

#3(3
# print(dir(1))

#3(4
# a = "hello"
# print(dir(a))

#4
# print(abs(-4))
# print(abs(10))

#5
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
#
# print(all([1,2,3]))
# print(all([1,0,20,30]))

#6
# print(any([0,'']))
# print(any([0,0,0,1,0]))



#7
# print(bin(3))
# b=bin(3)
# print(type(b), b[2:])
# print(bin(-10))
# print(format(14,'#b'),format(14,'b'))
# print(f'{14:#b}',f'{14:b}')


#8
# print(abs(10))
# print(abs(-10))
# print(bool(0))
# print(bool(1))
# print(bool(None))
# print(bool('a'))

#9
# print(chr(97))
# print(chr(122))
# print(chr(13))
# print(chr(13))
# print(chr(48))

#10
# print(ord('a'))
# print(ord('0'))

#11
# print(divmod(7,3))

#12
# for i,a in enumerate(['body','foo','bar']):
#     print(i,a)

#13
# myTup = (56,79,82,1,22,99)
# print(max(myTup),min(myTup))
#
# print('영문자 중 가장 큰 문자:',max('abcde'))
# print('서로 다른 문자들 중 큰 문자:',max('0Aa'))
#
# print('문장 속 최댓값 문자:', max('I went to the zoo yesterday, 27 March'))
# print('문장 속 최솟값 문자 : ',min('I went to the zoo yesterday, 27 March'))
#


#14
# a = [1,2,3,4,5]
# b = (1,2,3,4,5)
# print(sum(a),sum(b))
# print(sum(a,10))

#15
# a1 = int('aa',16)
# a2 = int('56',8)
# a3 = int('10',2)
# print(a1,a2,a3)

#16
# a1 = bin(30)
# a2 = bin(15)
# a3 = bin(10)
# print(a1)
# print(a2)
# print(a3)

#17
# a = bytes(10)
# print(a)
# b = bytes(b'1A0a')
# print(b)
# print(b[1])

#17,21,22

#18
# myNumber = [10,20,30,40,50]
#
# for n in myNumber:
#     print(bin(n)[2:])

#19
# myNumber = [10,20,30,40,50]
# for n in myNumber:
#     print(hex(n))

#20
# myNumber = [10,20,30,40,50]
# for n in myNumber:
#     print(oct(n))

#23
# print(pow(2,4))
# print(pow(3,3))

#24
# print(pow(10,2))
# print(round(2.3), round(4.6))
#
# mylist= [1,2,3,4,5,6]
# print(sum(mylist))

#25
# it =iter([1,2,3,4,5])
# print(next(it))
# print(next(it))
# print(next(it))

#26 질문
# items = [1,2,3,4,5]
# L1 = []
# for i in items:
#     L1.append(i**2)
# print(L1)
#
# def f(x):
#     return x*x
#
# L2 = list(map(f, items))
# print(L2)
#
# L3 = list(map(lambda x: x*x, items))
# print(L3)

#27 round 부문 2.5 가 왜 2로 되는지
#
# print(round(x))
# a = [1.2,2.5,3.7,4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)
#
# b = [1.2,2.5,3.7,4.6]
# b = list(map(lambda x : round(x),b))
# print(b)

# x=2.55
# print(round(x, 2))



# #28 리스트 위치가 왜 중요한지
# X = range(10)
# y = list(map(lambda x : x*x + 4*x +5 , X))
# print(y)


#29
# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# z = list(map(lambda x,y: x+y, x,y))
# print(z)

#30
# import operator
# X = [1,2,3,4,5]
# Y = [6,7,8,9,10]
# Z = list(map(operator.add,X,Y))
# print(Z)

#31
# items = [1,2,3,4,5]
# squared = list(map(lambda x : x**2,items))
# print(squared)

# items = [1,2,3,4,5]
# squared = [x**2 for x in items]
# print(squared)

#32
# names = ["Kim dss",'Park python','Lee sceince','Jung school']
# result = list(map(lambda name: name.split()[1],names))
# print(result)

#33
# f = filter(lambda x : x>2 , [1,2,3,34])
# print(list(f))

#34
# L = [1,2,3,4,5,6,7,8,9]
# f = list(filter(lambda x : x%2 == 0 , L))
# print(f)

#35
# number_list = range(-5,5)
# less_than_zero = list(filter(lambda x : x < 0,number_list))
# print(less_than_zero)

#36
# x = list(range(-5,5))
# print(x)
# print(list(filter(lambda y : y<0,x)))
# print(list(filter(lambda y : y>0 , x)))
# print(list(filter(None,x)))

#37
# L = ['high','Level','bulit_in','function','',None]
# print(list(filter(None,L)))

#38
# names = ['Kim dss','park python','lee science','jung school','lee java']
# names = list(map(lambda name : name.capitalize(), names))
# result = list(filter(lambda name : name.startswith('Lee')==True, names))
# print(result)

#39
# ls1 = [1,2,3,4]
# ls2 = [5,6,7,8]
# ls3 = [9,10,11,12]
#
# def sum_func1(*args):
#     return sum(args)
#
# def map_func(func,*args):
#     result = []
#     values_count =len(args[0])
#     for idx in range(len(args)):
#         values_count = values_count if values_count < len(args[idx]) else len(args[idx])
#
#     params_count = len(args)
#     for idx_1 in range(values_count):
#
#         params = []
#         for idx_2 in range(params_count):
#             params.append(args[idx_2][idx_1])
#         result.append(func(*params))
#     return result
# print(map_func(sum_func1, ls1, ls2, ls3))


#40
# number_list = range(-5,5)
# less_than_zero = [x for x in number_list if x < 0 ]
# print(less_than_zero)

#41
# X = [1,2,3]
# Y = ['a','b','c']
# a=list(zip(X,Y))
# A,B = zip(*zip(X,Y))
# print(A)
# print(B)

#42
# X = [1,2,3]
# Y = ['a','b','c']
# Z = list(zip(X,Y))
# print(Z)
# print(list(zip(*Z)))

#43
# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']
#
# for x,y in zip(a,b):
#     print(x,y)
#
# c = list(zip([1,2,3],[4,5,6]))
# d = list(zip([1,2,3],[4,5,6],[7,8,9]))
# e = list(zip("abc",'def'))
# print(c)
# print(d)
# print(e)

#44
# names = ['Prodo','cecilia','Sally','Neo']
# letters = [len(n) for n in names]
# longest_name = None
# max_letter = 0
# for name,count in zip(names,letters):
#     if count > max_letter:
#         longest_name = name
#         max_letter = count
# print(longest_name)

#45
# from itertools import zip_longest
# x = [1,2,3]
# y = [4,5,6,7]
#
# z1 = list(zip(x,y))
# print(z1)
#
# z2 = list(zip_longest(x,y))
# print(z2)
#
# z3 = list(zip_longest(x,y,fillvalue=0))
# print(z3)

#46
# def add_expr(a,b):
#     return str(a) + ' + ' + str(b)
#
# s = add_expr(3,5)
# print(s)

#47
# a1 = repr(3)+repr(4)
# print(a1)
# s2 = repr([1,2,3])
# print(type(s2))
# print(s2)

#48
# print(eval('1000 * 2'))
# number = 1
# exp = 'print(number + 1)'
# eval(exp)

#49
# print(eval('1+2'))
# print(eval("'hi'+'a'"))
# print(eval('divmod(4,2)'))

#50
# state1 = 'print("I Love Python")'
# exec(state1)
# state2 = '''
# number = 1
# for item in [1,2,3]:
#     number +=1
#     if item%2:
#         break
# print(number)
# '''
#
# exec(state2)
# a = 0
# exec('a = 2+3-2')
# print(a)


#51
# def reduce(function, iterable,initializer = None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#
#     return value
#
# def sum(x,y):
#     return x+y
#
# print(reduce(sum, [1,2,3,4,5]))


#52
# ls = [1,2,3,4,5,6,7,8,9,10]
# def reduce_func(func, data_list):
#     result = data_list[0]
#     for i in range(1,len(data_list)):
#         result = func(result,data_list[i])
#     return result
# print(reduce_func(lambda num1, num2: num1 + num2, ls))

#53
# from functools import reduce
# print(reduce(lambda x,y  : x+y, [1,2,3,4]))
# print(reduce(lambda x,y : x*y, [1,2,3,4]))

#54
# from functools import reduce
# ls = [1,2,5,8,3,4,7]
# max = reduce(lambda x,y : x if x>y else y, ls)
# print("max=",max)

#55
# sum_value = 0
# for i in range(1,10):
#     sum_value += i
# print(sum_value)

# from functools import reduce
# print(reduce(lambda x, y : x+y, [x for x in range(1,101)]))

#56
# number = 0
# exp = 'number + 1'
# code1 = compile(exp, '<string>','eval')
# for h in range(100):
#     number = eval(code1)
# print('1',number)
#
# state1 = 'number = number +1'
# code2 = compile(state1,'<string>','single')
# for h in range(100):
#     exec(code2)
# print('2',number)
#
# state2 = '''
# for item in [1,2,3]:
#     number = number+1
#     if item ==2:
#         break
# print('3',number)
# '''
#
# code3 = compile(state2,'<string>','exec')
# exec(code3)

#56
# number = 0
# exp = 'number + 1'
# code1 = compile(exp,'<string>','eval')
# for h in range(100):
#     number = eval(code1)
# print('1',number)
#
# state1 = 'number = number + 1'
# code2 = compile(state1, '<string>','single')
# for h in range(10):
#     exec(code2)
# print('2',number)
#
# state2= '''
# for item in [1,2,3]:
#     number = number + 1
#     if item == 2:
#         break;
# print('3',number)
# '''
#
# code3 = compile(state2,'<string>','exec')


#57
# class Person:
#     pass
#
# a = Person() #instance, object,변수, 객체
# print(type(a))
# print(isinstance(a,Person))



#58 오류
# calss fooboo(object):
#     def __init__(self,val):
#         self.val = val
#
# class gooboo(fooboo):
#     def __init__(self, val, val2):
#         self.val = val
#         self.val2 = val2
#
# o1=fooboo(10)
# j1=gooboo(11,22)
# print(issubclass(gooboo, fooboo))
# print(issubclass(fooboo, gooboo))
# print(issubclass(fooboo,object))


#59
# class A(object):
#     '''
#     class A
#     '''
#     def __init__(self):
#         print('init class A')
#
#     def get_name(self):
#         return 'class A'
#
# class B(A):
#     '''
#     class B
#     '''
#     def __init__(self):
#         print('init class B')
#
#     def get_super_name(self):
#         super().get_name()
#
# b = B()
# print(b.get_name())


#60
# help(sum)

#61
# def func(a):
#     if a > 10 :
#         return 'a가 10보다 크다'
#     else:
#         return 'a가 10보다 작다'
# print(func(3))

#61(2

# def func2(a):
#     return 'a가 10보다 크다' if a>10 else 'a가 10보다 작다'
#
# print(func2(3))


#HW 1
# print(list(range(5)))
# print(list(range(5,10)))
# print(list(range(1,11,2)))
# print(list(range(0,-10,-1)))

#HW 2
# num = [1,7,4,6,8,9,2,5]
# print(max(num))
# print(min(num))

#HW 3
# list1 = [1,2,3,4,5]
# list2 = [0,1,2,3,4,5]
# print(all(list1))
# print(all(list2))

#HW 4
# num = [2,3,1,7,10,4,5,8]
# print(sorted(num))
# print(sorted(num,reverse = True))

#HW 5
# List = [10000,10500,10300,10700, 11100]
# print(sum(List)/len(List))

#HW 6
# a,b = map(int,input('2개의 정수입력 : ').split())
# print(divmod(a,b))

#HW 7
# a = input('문장을 입력 하세요 : ')
# a1= a.split(' ')

# print(len(a1))

#HW 8
# a = input('문자열 입력 : ')
#
# for i in range(97,123):
#     print(chr(i),':',end=' ')
#     if (chr(i) in a)== True:
#         print(a.find(chr(i)))
#     else:
#         print(-1)

#HW 9
# List = ['0000600','034560','003540','039490']
# a = ';'.join(List)
# print(a)

#HW 10
# List = ['body','foo','bar','dfs','dfx']
# for i,k in enumerate(List):
#     print(i,k)


#HW 11
# seqList = [1,2,4,3,5]
# array = [0,10,20,40]
#
# print(sorted(seqList,reverse=True))
# for i in reversed(array):
#     print(i)

#HW 12
# sList = [5,3,1,2,4]
# print(sorted(sList))
# print(sorted(sList,reverse = True))

#HW 13
# s = "This is a test string from Andrew"
# student_tupples = [('john','A',15),('jane','B',12),('dave','B',10)]
# s1=sorted(student_tupples,key=lambda x: x[2], reverse=True)
# print(s1)


#HW 14 질문
# students = [('홍길동',3.9,2016303),('김철수',3.0,2016302),('최아리',4.3,2016301)]
# s1 = sorted(students, key = lambda x : x[2])
# print(s1)
# s2 = sorted(students, key = lambda x : x[2],reverse= True)
# print(s2)

#HW 15
# ls  = [1,2,3,4,5]
# print(list(map(lambda x : x-1, ls)))

#HW 16
# a,b = map(float,input('두개의 수 입력 : ').split())
# print(a, '+',b, '=', a+b)
# print(a, '-', b,'=',a-b)
# print(a,'*',b,'=',a*b)
# print(a,'/',b,'=',a/b)

#HW 17
# a = [1.2,2.5,3.7,4.6]
# a1 = list(map(int,a))
# print(a1)

#HW 18
# x = [1,2,3,4,5]
# x1 = list(map(lambda x : x*x, x))
# print(x1)

#HW 19
# x = [1,2,3,4,5]
# x1 = list(map(lambda y : y*2, x))
# print(x1)

#HW 20
# print(list(map(str, list(range(10)))))


#HW 21
# ls1 = [10,20,30,40]
# ls2 = [1,2,3,4]
# x = list(map(lambda x,y: x*y, ls1,ls2))
# print(x)

#HW 22
# s = 'as soon as possibl'
# s1= s.split()
#
# k = list(map(lambda x : x[0], s1))
# k1 = ''.join(k)
# print(k1)

#HW 23
# x = [1,2,3]
# y = [4,5,6,7]
# print(list(zip(x,y)))

#HW 24
# x = [1,2,3]
# y = [4,5,6]
# z = [7,8,9]
# a = 'abc'
# b = 'def'
# print(list(zip(x,y)))
# print(list(zip(x,y,z)))
# print(list(zip(a,b)))

#HW 25

# d = {'banana':3,'apple':4,'pear':1,'orange':2}
# d1 = d.keys()
# d2 = d.values()
# d3 = list(zip(d2,d1))
# print(max(d3,key = lambda x: x[0]))
# print(min(d3))
# d4 = list(sorted(d3, key = lambda x : x[0]))
# d5 = list(sorted(d3,reverse = True))
# print(d4)
# print(d5)



#HW 26
# L = [1,2,3,4,5,6,7]
# L1 = list(filter(lambda x: x<4, L))
# print(L1)


#HW 27
# list1 = [1,-3,2,9,0,-5,6]
# L = list(filter(lambda x: x>0, list1))
# print(L)

#HW 28
# L = 'abcABCdefDEF'
# L0 = list(L)
# L1 = list(filter(lambda x : 65<=ord(x)<=90, L0))
# print(''.join(L1))

#HW 29
# L = list(range(100))
# L1 = list(filter(lambda x: x%5 == 0 or x%7 ==0, L))
# print(L1)


#HW 30
# L = {'kim sook','Lee science','park min joo','Lee java'}
# L1 = list(L)
# L2 = list(filter(lambda x: x.startswith('Lee'),L1))
# print(L2)

#HW 31
# fnames = ['a_thumb.jpg','b01_thumb.jpg','s100_thumb.jpg','S100.jpg','b01.jpg']
# fnames1 = list(filter(lambda x: ('thumb' in x)==True , fnames))
# fnames2 = list(filter(lambda x: ('thumb' in x)==False , fnames))
# print(fnames1)
# print(fnames2)


#HW 32
# xs = list(range(10))
# print(list(map(lambda x : x*2,xs)))
# print(list(map(lambda x : (x+1)**2,xs)))
# print(list(filter(lambda x : x%2 == 0 , xs)))


#HW 33
# l = []
# a = input('문자열 입력 : ')
# for i in range(97,123):
#     l.append((chr(i),a.count(chr(i))))
# l1 = list(sorted(l,key = lambda x: x[1], reverse = True))
# print(l1[0][0])


#HW 34
# a = list(range(1,11,1))
# b = list(filter(lambda x : x%2 == 0, a))
# c = list(set(a)-set(b))
# print(c,b)


#HW 35
# from functools import reduce
# a = [1,2,3,4,5]
# print('5! =',reduce(lambda x,y: x*y, a))


#HW 36 질문 민지가 안뽑히고 샐리뽑힘같은 글자수
# l = ['Sally','Hong gil dong','Gwon Yeji','Minji','Lee sun sin']
# print('가장 긴 이름 :',max(l,key=lambda x: len(x)))
# print('가장 짧은 이름 :',min(l,key= lambda x: len(x)))


#HW 37
# a = input('식을 입력 하세요 : ')
# a1 =compile(a, '<string>','eval')
# print(eval(a1))


#HW 38
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# a = '{} + {}'.format(min(l1),max(l2))
# print(a,'=',eval(a))


#HW 39 질문
# a = input('방번호 : ')
# a = list(a)
# list = []
# for i in range(0,10,1):
#     list.append(a.count(str(i)))
#
# list[9]=int((list[6]+list[9])/2+0.5)
# list[6]=0
#
# print('{}개의 세트가 필요합니다'.format(max(list)))

#HW 40
# code1 = '30 1 21 17 28'
# code2 = '9 20 28 18 11'
# c1list = code1.split()
# c2list = code2.split()
# print(c1list)
# print(c2list)
# c1binary = list(map(lambda x : bin(int(x))[2:], c1list))
# c2binary = list(map(lambda x : bin(int(x))[2:],c2list))
# c1sep = []
# c2sep =[]
# for i in c1binary:
#     if len(i)==5:
#         for k in range(5):
#             c1sep.append(int(i[k]))
#     else:
#         for j in  range(5-len(i)):
#             c1sep.append(0)
#         for l in range(len(i)):
#             c1sep.append(int(i[l]))
# for i in c2binary:
#     if len(i)==5:
#         for k in range(5):
#             c2sep.append(int(i[k]))
#     else:
#         for j in  range(5-len(i)):
#             c2sep.append(0)
#         for l in range(len(i)):
#             c2sep.append(int(i[l]))
#
#
#
# print(c1binary)
# print(c2binary)
# print(c1sep)
# print(c2sep)
#
# totalbinary = list(map(lambda x,y: ' ' if x==y==0 else '#', c1sep,c2sep))
# print(totalbinary)
# for i in range(len(totalbinary)):
#
#     print(totalbinary[i],end='')
#     if (i+1)%5==0:
#         print()








#
# code1 = '30 1 21 17 28'
# code2 = '9 20 28 18 11'
# c1list = code1.split()
# c2list = code2.split()
#
# totalsep=[]
# totalbinary= list(map( lambda x,y : bin(int(x)|int(y))[2:],c1list,c2list))
#
#
# for i in totalbinary:
#     if len(i)==5:
#         for k in range(5):
#             totalsep.append(int(i[k]))
#
# totalbinary1 = list(map(lambda x: ' ' if x==0 else '#', totalsep))
#
# for i in range(len(totalbinary1)):
#     print(totalbinary1[i],end='')
#     if (i+1)%5==0:
#         print()



#HW 41
#
# a1 = [1,2,3,4,5]
# a2 = [2,1,2,3,2]
# a3 = [3,3,1,1,2]
#
# def firstplace():
#     n1 = 0
#     n2 = 0
#     n3 = 0
#
#     import random
#     answer = []
#     for i in range(5):
#         answer.append(random.randint(1,5))
#         if a1[i] ==answer[i]:
#             n1+=1
#         if a2[i] ==answer[i]:
#             n2+=1
#         if a3[i] ==answer[i]:
#             n3+=1
#
#     a = sorted([(a1,n1),(a2,n2),(a3,n3)],key=lambda x : x[1])
#     a1st= []
#     for i in range(3):
#         a1st.append(i+1)
#         if a[i] != a[i+1]:
#             break
#
#     return '{}        {}'.format(answer,a1st)
# print('answer(정답)            return')
# print(firstplace())
# print(firstplace())












# lsy = 1
# dd = 0        #随便取啥，不要是关键字
# while True:
#     n = int(input('请输入第{}科成绩:'.format(lsy)))
#     if n > 100 or n < 0:
#         print('请重新输入')
#         continue
#     dd = dd + n
#     if lsy >= 5:
#         print("总成绩为:{},平均成绩为:{}".format(dd,dd/lsy))
#         break
#     lsy += 1
#
# '随机数获取：百度  python3 random 关键字，查询资料获得'
# '6、打印100-999中不能被7整除又不包含7的数'


# lsy = 1
# dd = 0        #随便取啥，不要是关键字
# while True:
#     n = int(input('请输入第{}科成绩:'.format(lsy)))
#     dd = dd + n
#     if lsy >= 1:
#         print("平均成绩为:{}".format(dd,dd/lsy))
#         break
#     lsy += 1

#lsy = 1
# dd = 0        #随便取啥，不要是关键字
# while True:
#     n = int(input('请输入第{}科成绩:'.format(lsy)))
#     if n > 100 or n < 0:
#         print('请重新输入')
#         continue
#     dd = dd + n
#     if lsy >= 5:
#         print("总成绩为:{},平均成绩为:{}".format(dd,dd/lsy))
#         break
#     lsy += 1

# n1=1
# n2=2
# n3=3
# n4=4
# n5=5
# n6=6
# n7=7
# n8=8
# n9=9
# print("1*1={}".format(n1*n1))
# print("1*2 ={}| 2*2={}".format(n1*n2,n2*n2))
# print("1*3={}|2*3={}|3*3={}".format(n1*n3,n2*n3,n3*n3))
# print("1*4={}|2*4={}|3*4={}|4*4={}".format(n1*n4,n2*n4,n3*n4,n4*n4))
# print("1*5={}|2*5={}|3*5={}|4*5={}|5*5{}=".format(n1*n5,n2*n5,n3*n5,n4*n5,n5*n5))
# print("1*6={}|2*6={}|3*6={}|4*6={}|5*6={}|6*6={}".format(n1*n6,n2*n6,n3*n6,n4*n6,n5*n6,n6*n6))
# print("1*7={}|2*7={}|3*7={}|4*7={}|5*7={}|6*7={}|7*7={}".format(n1*n7,n2*n7,n3*n7,n4*n7,n5*n7,n6*n7,n7*n7))
# print("1*8={}|2*8={}|3*8={}|4*8={}|5*8={}|6*8={}|7*8={}|8*8={}".format(n1*n8,n2*n8,n3*n8,n4*n8,n5*n8,n6*n8,n7*n8,n8*n8))
# print("1*9={}|2*9={}|3*9={}|4*9={}|5*9={}|6*9={}|7*9={}|8*9={}|9*9={}".format(n1*n9,n2*n9,n3*n9,n4*n9,n5*n9,n6*n9,n7*n9,n8*n9,n9*n9))

# i = 1
# while i <= 9:
#     j = 1
#     x =''
#     while j <= 10-i:
#         x += ('{0:d} x {1:d} = {2:2d} |'.format(i,10-j,i*j))
#         j += 1
#     print(x)
#     i+= 1


# i = 1
# while i <= 9:
#     j = 9
#     x = ""
#     while j >= i:
#         x +="{0:d} x {1:d} = {2:2d}|".format(i,j,i*j)
#         j -= 1
#     print(x)
#     i +=1


# print('{0:7d}'.format(1))
# print('{0:5d}{1:4d}'.format(2,3))
# print('{0:3d}{1:4d}{2:4d}'.format(4,5,6))
# print('{0:1d}{1:4d}{2:5d}{3:4d}'.format(7,8,9,0))

# i = 1
# n = 5
# space_num = n -1
# while space_num >= 0:
#     string = (' '*space_num)
#     j = 0
#     while n - space_num > j:
#         string += str(i%10) + " "
#         i += 1
#         j += 1
#     print(string)
#     space_num -= 1

#
# kongge = 6
# xinghao = 1
# j = kongge
# while kongge > 0:
#     daan = (j*' ')
#     while xinghao < 6:
#         daan += str(kongge%10) +'*'
#     print(daan)
#     j -=1
#     xinghao =+1

# i = 6
# while i > 0:
#     print('*'*i)
#     i -= 1

# i = 1
# n = 9
# space_num = n -1
# while space_num >= 0:
#     string = (' '*space_num)
#     j = 0
#     while n - space_num > j:
#         string += str(i%10) + " "
#         i += 1
#         j += 1
#     print(string)
#     space_num -= 1


# i = 7
# n = 1
# kongge = i-1
# xing = n + 1
# while kongge > 0:
#     while xing < 8:
#         kongge = (i - 1)
#         kongge -= 1
#         xing +=1
#     print(kongge*' '+xing*'*')


#====================================错误
# lines = 6
# kongge = 6
# j =lines
# while j >= 0:
#     kongge = lines -kongge
#     print(' '*kongge+'*'*j)
# j -= 1
# kongge += 1


#         菱形*形
#

# lines =6
# star_num =6
# j = lines
# while j > 0:
#     space_num = lines -star_num
#     print(' '*space_num+'*'*star_num)

#========================================错误

#名字的规则和变量的一样
# def mingzi(n):
#
#     if n % 2 == 0:
#         raise  Exception('必须是技术')
#     mid = n // 2 + 1  # 中间一排
#     i = 1
#     while n > 0:
#         space_num = abs(mid - i)
#         base_num = mid - space_num
#         star_num = base_num * 2 - 1
#         if base_num !=1:
#             print(' ' * space_num + '*' +' '* (star_num-2)+'*')
#         else:
#             print(' '*space_num +'*')
#         i += 1
#         n -= 1
#
# mingzi(15)

# def is_prime(n):
# #    i = 20
#     flag = True
#     while n > i:
#         if not n % 3:
#             flag = False
#             break
#         i += 1
#     return flag
#
# number = 100
# while number > 0:
#     if is_prime(number):
#         print(number)
#     number -=1

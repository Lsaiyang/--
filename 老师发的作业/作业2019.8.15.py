

'备注：循环嵌套练习题根据学生情况选择'


'循环嵌套练习题：'

'1、求 100-200以内同时能被2、3、5整除的第一个数'
# i =100
# j =200
# while j >= i:
#     if (not i % 2) and (not i % 3) and (not i % 5):
#         print(i)
#         break
#     i += 1

'3、9*9乘法表输出'
# i = 1
# while i <= 9:
#     j = 1
#     x =''
#     while j <= i:
#         x += ('{0:d} x {1:d} = {2:2d} |'.format(j,i,i*j))
#         j += 1
#     print(x)
#     i+= 1

'4、求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'
# n =int (input('数字：'))
# total = 0
# a ='2'
# while n > 0:
#     number = a*n
#     # 0 = '2222'
#     total += int(number)
#     n -= 1
# print(total)

'5、一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？'
# i=10
# total = 0
# h = 100       #数值有问题
# while i >0:
#     total += h
#     h = h/2
#     total += h
#     i -= 1
# print(h)
# print(total)

'5、打印以下图形：'
# print('{}{}{}{}{}{}{}{}{}'.format('*','*','*','*','*','*','*','*','*'))
# print('{}{}{}'.format('*'," "*7,'*'))
# print('{}{}{}'.format('*'," "*7,'*'))
# print('{}{}{}{}{}{}{}{}{}'.format('*','*','*','*','*','*','*','*','*'))
'   *********   '
'   *       *   '
'   *       *   '
'   *********   '

# w = 14  # 长度
# h = 10  # 高度
# i = h
# while i > 0:
#     if h == i or i == 1:
#         print('*' * w)
#     else:
#         print('*' + " " * (w - 2) + '*')
#
#     i -= 1
      
'''
*******
 *****
  ***
   *
  ***
 *****
*******
'''
# n = 12
# i = 1
# mid = n//2 + 1 #中间
#
# while n >= i:
#     if i <= mid:
#         space_num = i - 1
#         base_num = mid + 1 - i
#     else:
#         space_num = n - i
#         base_num = i - mid + 1
#
#     star_num = base_num * 2 - 1
#     print(" "*space_num + '*'*star_num)
#     i += 1

'''
     A
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
ABCDEFEDCBA
'''

# i = 0
# floor = 6
# bias = 64
# while i < floor:
#     space_num = floor - i #空格数量
#     k = 1  #需要循环的次数
#     j = i - 1
#     string = ""
#     while k < 2*i:
#         if k <= i:
#             num = k
#         else:
#             num = j
#             j -= 1
#         k += 1
#         string += chr(num + bias)
#     i += 1
#     print(" "*space_num + string)

'''
******
*****
****
***
**
*
'''
i = 1
while i < 6:
     print("*"*i)
     i += 1
#        打印三角形*2
while i > 0:
    print('*'*i)
    i -= 1
# print('{0:7d}'.format('A'))
# print('{0:5d}{1:4d}'.format(2,3))
# print('{0:3d}{1:4d}{2:4d}'.format(4,5,6))
# print('{0:1d}{1:4d}{2:5d}{3:4d}'.format(7,8,9,0))











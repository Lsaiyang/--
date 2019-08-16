'练习：根据课堂情况可用作课堂练习或者课后练习'
'1、判定一个输入的整数是否为偶数'
# n = input('n哪个输')
# n=int (n)
# if n % n:
#     print('jishu')
# else:
#     print(oushu)
'2、验证自己是否成年(18岁及以上属于成年)'
# age = input('please enter age')
# age =int(age)
# if age >= 18:
#     print('adult')

# n=int(input('你的年龄:'))
# if 0 < n < 18:
#     print('未成年')
# else:
#     print('成年')


'3、闰年问题（输入一个年份，判断是否为闰年）'
'能被4整除 不能被100整除'
'或者能被400整除'
# while True:
#     年份 = input('哪一年:')
#     年份 = int(年份)
#     if not 年份 % 400 :
#         print('闰年')
#     elif (年份 % 4 == 0)and(年份 % 100):
#         print('闰年')
#     else:
#         print('平年')

'4、小明身高1.75，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：'
# def bmi(tizhong,shengao):
#     return  tizhong/(shengao**2)
# tizhong = int(input('tizhong:'))
# shengao = (input('shengao'))
#
# res = bmi (tizhong,shengao)
#
# if res < 18.5:
#     print('过轻')
# elif res < 25:
#     print('zhengchang')
# elif res < 28:
#     print('feipang')
# elif res <32:
#     print('yanzhongfeipang')
# （1）低于18.5：过轻
# （2）18.5-25以下：正常
# （3）25-28以下：过重
# （4）28-32：肥胖
# （5）高于32：严重肥胖
'5、购买车票，输入身高，判定1.2m以下输出购买儿童票；其他输出成人票'
# n = (input('你的身高：'))
# if n >= 1.2:
#     print('成人票')
# elif n < 1.2:
#     print('儿童票')


'6、输入温度，查看温度适宜问题（15度以下寒冷，15-29度舒适，30度及以上炎热)'
# n=int (input('当前温度：'))
# if n < 15:
#     print('寒冷')
# elif 15 <= n <29:
#     print('舒适')
# elif 30 < n:
#     print('炎热')
'7、输入年龄，验证该年龄是否成年(18岁及以上属于成年)'
# n=int (input('多少岁：'))
# if n < 18:
#     print('未成年')
# elif n >= 18:
#     print('成年')
'8、今天老板找我到办公室，说要调整薪资，输入老板说的薪资，输出我此刻的心情（条件和心情自由设定）'
# qian = int(input('薪资:'))
# if qian < 8888:
#     print('明天不上班')
# elif qian < 12000:
#     print('不爽')
# elif qian >12000:
#     print('可以')

# n=int(input('给你薪资：'))
# if n < 200000000:
#     print('心情不好')
# elif n >200000000:
#     print('心情好')
'9、输入一个成绩，如果考试成绩大于 90 分，则奖励一个 IPHONE 8S ，如果成绩介于 70 分至 90 分之间，则奖励一个小米，否则罚做 500 个俯卧撑。'
# n=int(input('成绩：'))
# if n <70:
#     print('奖励500俯卧撑，恭喜恭喜')
# elif n >= 90:
#     print('奖励IPHONE 8S')
# elif 70 < n < 90:
#     print('奖励小米')
'10、在游乐场中，门票全票价位10美元'
'4岁以下免费；'
'4~18岁收费3美元；'
'18岁（含）以上收费10美元。'
'对于65岁（含）以上的老人，可以半价（即5美元）购买门票，输入年龄，查看需要多钱购买门票'
# n=int (input('年龄：'))
# if n<4:
#     print('免费')
# elif 4 < n < 18:
#     print('收费3美元')
# elif n >= 18:
#     print('收费10美元')
# elif n >65 :
#     print('半价10美元')
'提升：'
'1、某单位马上要加工资，增加金额取决于工龄和现工资两个因素：'
'#对于工龄大于等于20年的，如果现工资高于2000，加200元，否则加180元；'
'#对于工龄小于20年的，如果现工资高于1500，加150元，否则加120元。工龄和现工资从键盘输入，编程求出一个员工加工资后的工资。'
# n = int(input('请输入工龄：'))
# qian = int(print('qingshurugongzi :'))
#
# if n >= 20:
#     if qian >2000:


'2、请写1个ATM程序.定义1个变量,用来存储该ATM机器中剩余的金额.'
'1)接收用户输入取款金额.由于ATM机器只支持100的票子.'
'2)如果用户输入的取款金额不是100的倍数的话.则打印 "对不起,本机器无法提供输入的面额"'
'3)如果用户输入的取款金额大于了ATM的剩余金额.则打印 "对不起,余额不足."'
'4)如果用户输入的取款金额是100的倍数,并且小于等于ATM的剩余金额就打印."正在出钞,请从出钞口拿钱.ATM机器剩余xx元'
# atm_money = 10**4
# money = int(input('请输入要取钱的数量：'))
# if not money % 100:
#     if money > atm_money:
#         print('余额不足')
#     else:
#         print('正在出钞，请从嘲口拿钱，ATM剩余%d元') % (atm_money - money)
# else:
#     print('本机器无法提供面额')


'扩展内容：'
# 输入一个数，判定该数是否为质数
#❎
# n = int(input('请输入一个数'))
#
# i = 2
# flag = True
# while n > i :
#     if  not n % 1:
#         flag = False
#         print(i)
#         break
#     i += 1
# if flag:
#     print('是一个质数')
# else:
#     print('不是质数')


'1、求 100-200以内同时能被7、8整除的数'
#
# def fun1(n):
#     if n % 7 or n % 8:     #或if (not n % 7) and (not n % 8):
#         return False            #或True
#     else:
#         return True           #或False
# n = 100
# while n < 201:
#     if fun1(n):
#         print(n)
#     n += 1

' 2、求 1-100以内所有含6的数'
# def fun1(n):
#
#     n1 = n % 10 #个位数
#     n2 = n // 10 #十位数
#     if n1 == 6 or n2 == 6:
#         return True
# n = 1
# while n < 100:
#     if fun1(n):
#         print(n)
#     n += 1

'3、使用while和if  ，实现求100以内，个位数和十位数相等的两位数'
# 错
# def fun1(n):
#     n1 = n %10
#     n2 =n//10
#     if n1 == n2:
#         return  True
# n =1
# while n < 100:
#     if fun1(n):
#         print(n)
#         n+=1

' 基础提升'
' 1、求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100'
# n = 0
# total = 0
# while n <= 100:
#     if n % 2:
#         total+= -n
#     else:
#         total += n
#     n +=1
# print(total)

' 2、Chuckie Lucky赢了100W美元，'
'他把它存入一个每年盈利8%的账户。'
'在每年的最后一天，Chuckie取出10W美元。'
'编写一个程序，计算需要多少年Chuckie就会清空他的账户。'
# money = 200
# n = 1
# while True:
#     money = money * 1.05
#     money = money - 10
#     if money <= 0:
#         print(money)
#         break
#     print(money)
#     n += 1
# print(n-1)

'循环退出练习题：'
'1、银行登录案例'
'3、循环输入7天温度，求平均温度'
'4、依次输入几个数据，直到0作为输入的结束， 然后求出输入的这些数据的总和及平均值（0不算次数）；'

'5、求1000-5000之间，各位数字之和为5的所有整数，打印输出（例如整数2003的各位数字之和为2+0+0+3，等于5）'
# def test(n) :
#     n1 = n // 1000
#     n2 = n // 100 % 10
#     n3 = n // 10 % 100
#     n4 = n % 10
#     if n1 + n2 +n3 +n4 == 5:
#         return True
#     return  False
# n = 1000
# while n < 5001:
#     if test(n):
#         print(n)
#     n += 1
'2、输入班级学生语文成绩，求总成绩和平均成绩 。班级人数从键盘输入'
#           有问题
# i = 0
# total = 0
# while True:
#     n = input('input:')
#     n = int(n)
#     if n == 0:
#         print('总和%d 平均 %f' % (total,total/i))
#         break
#     total += n
#     i += 1

'提升：'
'1、从键盘输入10个数，求出最大数'
# n = int(input('number: '))
# i = 5
# while i > 1:
#     tmp = int(input('number: '))
#     if tmp > n:
#         n = tmp
#     i -= 1
# print(n)

'2、输入一个五位以内的数，求每位数字之和'
# def test(n):
#     n1 = n // 10000 % 10
#     n2 = n // 1000 % 10
#     n3 = n // 100 % 10
#     n4 = n // 10 %10
#     return n1 + n2 +n3 +n4 +n5
# n =int(input('number'))
# x =test(n)
# print(x)

'3、从键盘输入两个正整数，输出这个范围内的所有偶数： 如：输入 3 和9， 输出4 6 8'
# n1 = int(input('first: '))
# n2 = int(input('second: '))
# while n2 >= n1:
#     if not n1 % 2:
#         print(n1)
#     n1 += 1
'4、从键盘输入一个正整数x，打印输出从0开始的连续n个偶数，如 x = 5,输出 0 2 4 6 8'
# x = int (input('正整数：'))
# a = 0
# string = ''
# while x > 0:
#     string += str(a) +' '
#     a +=2
#     x -=1
# print(string)

'5、使用循环完成猜数字游戏，确定一个1-100的随机数（整数），提示用户输入数字进入猜的模式；'
' 输入数字后，如果与随机数（整数）相同，提示用户猜成功了；'
'输入数字后，如果与随机数（整数）不相同，提示用户猜大一点或者小一点；'\
'记录猜的次数，如果猜的次数小于三次，则赞赏，真聪明'
' 如果大于等于3次小于10次，则表示，要加油哦'
'随机数获取：百度  python3 random 关键字，查询资料获得'

import  random

number = random.randint(0,100)
i = 1
while True:
    n = int (input('数字：'))
    if n == number:
        break
    elif n > number:
        print('猜大一点')
    else:
        print('猜大一点')
    i += 1
if i < 3:
    print('真聪明')
elif i<-10:
    print('要加油哦')
else:
    print('瓜娃子')

'6、打印100-999中不能被7整除又不包含7的数'



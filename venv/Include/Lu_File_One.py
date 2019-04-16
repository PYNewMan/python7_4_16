import math
import keyword  # 查看系统保留的关键字，不可以用来进行重命名
import random

print(keyword.kwlist)

#向下取整
print(math.ceil(8.9))

# 向下取整
print(math.floor(7.1))

# round 四舍五入
print(round(5.5))
print(round(6.1))

# sqrt开平方，返回浮点数
print(math.sqrt(3.2))
print(math.sqrt(9))

# pow 与幂运算一样，一个数为低数，一个指数
print(math.pow(3,2))

print(4**2)
"""  幂运算返回整形  函数返回浮点数 """

# fabs() 对一个数值获取它的绝对值  返回的也是浮点数
print(math.fabs(-1))
print(math.fabs(0))
print(math.fabs(10))

# abs 获取绝对值的操作 不是数学模块当中的，而是Python内置的函数  返回的数值为字符本身
print(abs(-1))
print(abs(0))
print(abs(1.35567))

# fsum 与 sum 两个都为求和的函数 ，但一个带f是math函数内置的，另一个为python内置的
print(sum([1,2,3,4,5,7]))
print(math.fsum([10,9,8,7,6]))

# math.modf()  能够将一个浮点数，分别拆分为整数部分以及销售部分
"""
    一般拆分后，小数部分在前，而整数部分在后面
"""
print(math.modf(4.666))
help(math.modf)

# copysign() 将第二个数的（正负）符号，传递给第一个数
print(math.copysign(-2,8))

#  打印自然对数以及pi的数值
print(math.pi)
print(math.e)

"""
===========================================================================
"""

# random()   获取0到1之间的小数值，包括0，但不包括1

for i in range(7):

    print(random.random())
    print(random.randint(2,8))

print("""         ====================================
         ====================================
         ====================================""")
# random.randrange()  取指定开始以及到结束的数值，其之间的间隔值可指定，三个数值

for x in range(3):
    print(random.randrange(0,10,2))

# choice  获取列表当中的随机数值

#for num in range(3):

    print(random.choices([22,33,66,88,213,456,223]))

#  shuffle() 随机打乱序列  返回值是None
list1 = [1,3,4,6,7]
print(list1)
random.shuffle(list1)
print(list1)
# uniform() 随机获取之地奶牛关范围内的值，包括小数
print(random.uniform(1,4))

print("""==================================
------------------------------------------
===========================""")

sorce = input("请输入一个100内的数：")
if sorce.isdigit() and 1<< int(sorce) << 100:
    print("Yes!!")
else:
    print("No!!请按规定输入。")

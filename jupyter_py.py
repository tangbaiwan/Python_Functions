#!/usr/bin/env python
# coding: utf-8

# In[1]:


lambda l : l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])


# In[2]:


int('1010', 2)  


# In[3]:


"hi my name is Allwin".upper()  


# In[4]:


"Hi my name is Allwin".lower() 


# In[ ]:





# In[ ]:


# 使用“for”和“if”的列表解析


# In[5]:


[number for number in [1, 2, 3, 4] if number % 2 == 0]  # 使用“for”和“if”的列表解析


# In[ ]:





# In[ ]:


# 从列表中得到最长的字符串


# In[6]:


words = ['This', 'is', 'a', 'list', 'of', 'words']     # 从列表中得到最长的字符串
max(words, key=len)


# In[ ]:





# In[ ]:


# 反转列表


# In[7]:


numbers[::-1]


# In[ ]:





# In[ ]:


# 计算字符串中的某个字符出现的频率


# In[8]:


print("umbrella".count('l'))# 2


# In[ ]:





# In[ ]:


# 时间戳


# In[9]:


import time; print(time.time())


# In[ ]:





# In[ ]:


# 八进制转十进制


# In[10]:


int('30', 8)


# In[ ]:





# In[ ]:


# 将键值对转换为字典


# In[11]:


dict(name='allwin', age=23)


# In[ ]:





# In[ ]:


# 计算商和余数


# In[13]:


quotient, remainder = divmod(4,5)


# In[ ]:





# In[ ]:


#  获取一串小写字母


# In[14]:


import string; print(string.ascii_lowercase)


# In[ ]:





# In[ ]:


# 获取一串大写字母


# In[15]:


import string; print(string.ascii_uppercase)  


# In[ ]:





# In[ ]:


# 获取字符串类型的0到9的数字


# In[16]:


import string; print(string.digits)  


# In[ ]:





# In[ ]:


# 人类可读的日期时间


# In[17]:


import time; print(time.ctime())  


# In[ ]:





# In[ ]:


# 将列表元素的字符串类型转换为整型


# In[18]:


list(map(int, ['1', '2', '3']))  


# In[ ]:





# In[ ]:


# 从字符串中删除数字


# In[19]:


''.join(list(filter(lambda x: x.isalpha(), 'abc123def4fg56vcg2')))  


# In[ ]:





# In[ ]:


# 从列表中过滤偶数


# In[20]:


list(filter(lambda x: x%2 == 0, [1, 2, 3, 4, 5, 6] ))  


# In[ ]:





# In[ ]:


# 列表推导式


# In[21]:


def get_vowels(string):
    return [vowel for vowel in string if vowel in 'aeiou']
get_vowels('This is some random string')


# In[ ]:





# In[ ]:


# 计算代码执行时间


# In[23]:


import time

start_time = time.time()

total = 0
for i in range(10):
  total += i
print("Sum:", total)

end_time = time.time()
time_taken = end_time - start_time
print("Time: ", time_taken)


# In[ ]:





# In[ ]:


# 查找出现次数最多的元素


# In[25]:


def most_frequent(list):
  return max(set(list), key=list.count)

mylist = [1,1,2,3,4,5,6,6,2,2]
print("出现次数最多的元素是:", most_frequent(mylist))


# In[ ]:





# In[ ]:


# 检索列表最后一个元素


# In[28]:


my_list = ['banana', 'apple', 'orange', 'pineapple']

#索引方法
my_list[-1]

#pop方法
my_list.pop()


# In[ ]:





# In[ ]:


# 将两个列表转换为字典


# In[29]:


def list_to_dictionary(keys, values):
  return dict(zip(keys, values))

list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']

print(list_to_dictionary(list1, list2))


# In[ ]:





# In[ ]:


# 反转字符串


# In[30]:


str = "Hello World"

print("反转后字符串是:", str[::-1])


# In[ ]:





# In[ ]:


# 字符串列表组成单个字符串


# In[31]:


list = ["Hello", "world", "Ok", "Bye!"]
combined_string = " ".join(list)

print(combined_string)


# In[ ]:





# In[ ]:


# 返回字典缺失键的默认值  字典中的get方法用于返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。


# In[32]:


dict = {1:'one', 2:'two', 4:'four'}

#returning three as default value
print(dict.get(3, 'three'))

print("原始字典:", dict) 


# In[ ]:





# In[ ]:


# 正则表达式用来匹配处理字符串，python中的re模块提供了全部的正则功能。


# In[33]:


import re

text = "The rain in spain"
result = re.search("rain", text)

print(True if result else False)


# In[ ]:





# In[ ]:


# 统计字频      判断字符串每个元素出现的次数，可以用collections模块中的Counter方法来实现，非常简洁。


# In[38]:


from collections import Counter
result = Counter('banana')
print(result)


# In[ ]:





# In[ ]:


# 变量的内存占用


# In[39]:


import sys

var1 = 15
list1 = [1,2,3,4,5]

print(sys.getsizeof(var1))
print(sys.getsizeof(list1))


# In[ ]:





# In[ ]:


# 链式函数调用            在一行代码中调用多个函数。


# In[40]:


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 5, 10

print((add if b > a else subtract)(a,b))


# In[ ]:





# In[ ]:


# 科赫雪花


# In[43]:


import turtle
def kehe(len,n):
    if n == 0:
        turtle.fd(len)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            kehe(len / 3, n - 1)
lenth = 500
level = 3
du = 120
def main():
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pensize(2)
    turtle.color('green')
    turtle.pendown()
    kehe(lenth,level)
    turtle.right(du)
    kehe(lenth, level)
    turtle.right(du)
    kehe(lenth, level)
    turtle.right(du)
    turtle.hideturtle()
    turtle.done()


# In[44]:


from turtle import Turtle
t = Turtle()
t.speed(0)
#a = 180
b = 180
for c in range(5):
 	a = 9*c
 	for i in range(100):
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)
 		t.right(b)
 		t.circle(i,a)


# In[ ]:





# In[ ]:


# Python 直接将该入门程序做成了一个包。


# In[45]:


import __hello__


# In[ ]:





# In[ ]:


# 合并字符串


# In[46]:


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
''.join(x)


# In[ ]:





# In[ ]:


# 输出九九乘法表


# In[47]:


print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))


# In[ ]:





# In[ ]:


# 一行打印迷宫


# In[49]:


print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# 金字塔图案程序


# In[54]:


def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 反金字塔图案程序


# In[55]:


def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 正确启动模式程序


# In[56]:


def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end="")
           print("\r")
      for i in range(n, 0 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 左启动模式程序


# In[57]:


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 半金字塔图案程序


# In[64]:


def pattern(n):
     for i in range(0,n):
         for j in range(0, i+1):
              print("* " , end="")
         print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 左半金字塔图案程序


# In[67]:


def pattern(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0, k):
               print(end=" ")
          k = k - 2
          for j in range(0, i + 1):
              print("* ", end="")
          print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 向下半金字塔图案程序


# In[68]:


def pattern(n):
      for i in range(n, -1, -1):
           for j in range(0, i + 1):
               print("* ", end="")
           print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 菱形图案程序


# In[78]:


def pattern(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0 , k):
               print(end=" ")
          k = k - 1
          for j in range(0 , i + 1 ):
               print("* ", end="")
          print("\r")
     k = n - 2
     for i in range(n , -1, -1):
          for j in range(k , 0 , -1): 
               print(end=" ")
          k+= 1
          for j in range(0 , i + 1):
                print("* ", end="")
          print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:


# 沙漏图案程序


# In[106]:


def pattern(n):
     k = n - 2
     for i in range(n, -1 , -1):
        for j in range(k , 0 , -1):
            print(end=" ")
        k = k + 1   
        for j in range(0, i+1):
            print("* " , end="")
        print("\r")
     k = 2 * n  - 2
     for i in range(0 , n+1):
         for j in range(0 , k):
            print(end="")
         k = k - 1
         for j in range(0, i + 1):
            print("* ", end="")
         print("\r")   
pattern(5)


# In[ ]:





# In[ ]:


# 钻石星型


# In[88]:


for i in range(5):
    for j in range(5):
        if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
            print("*", end="")
        else:
            print(end=" ")
    print()


# In[ ]:





# In[ ]:





# In[ ]:


# 二进制数字模式程序


# In[107]:


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('10', end="")
 
        print("\r")
 
pattern(5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





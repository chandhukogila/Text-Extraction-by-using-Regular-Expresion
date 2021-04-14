#!/usr/bin/env python
# coding: utf-8

# In[1]:


height=float(input("enter the height: "))
weight=float(input("enter the weight: "))
bmi=weight/(height**2)
print(bmi)


# In[1]:


#we have money
j=float(input("enter the amount:"))

l=float(input("enter the interest per 100:"))
m=int(input("enter number of months:"))
interest=((j/100)*l)

print("interest per month",interest)
n=interest*m
print("interest for",m,"months is",n)



# In[2]:


x=67
y=80
x,y,z=1,2,3
print(x,y,z)


# **Intiger**

# In[1]:


h=150


# In[2]:


type(h)


# In[3]:


h.as_integer_ratio()


# In[5]:


h.bit_length()


# In[8]:


h.conjugate()


# In[11]:


h.denominator


# In[15]:


h.from_bytes()


# In[17]:


h.imag


# In[18]:


h.numerator


# In[20]:


h.real


# In[22]:


h.to_bytes()


# **Float**

# In[29]:


g=20.5


# In[30]:


type(g)


# In[31]:


g.as_integer_ratio()


# In[32]:


g.conjugate()


# In[44]:


g.fromhex()


# In[45]:


g.hex()


# In[46]:


g.imag


# In[48]:


g.is_integer()


# In[49]:


g.real


# **String**

# In[50]:


d="hello"


# In[51]:


type(d)


# In[52]:


d.capitalize()


# In[54]:


d.casefold()


# In[56]:


d.center(20)


# In[59]:


d.count('l')


# In[60]:


d.encode()


# In[62]:


d.endswith('o')


# In[64]:


d.expandtabs(20)


# In[65]:


d.find('o')


# In[68]:


d.format()


# In[72]:


d.format_map('20')


# In[74]:


d.index('l')


# In[78]:


d.isalnum()


# In[81]:


d.isalpha()


# In[82]:


d.isascii()


# In[83]:


d.isdecimal()


# In[84]:


d.isdigit()


# In[85]:


d.isidentifier()


# In[86]:


d.islower()


# In[87]:


d.isnumeric()


# In[88]:


d.isprintable()


# In[91]:


d.isspace()


# In[94]:


d.istitle()


# In[95]:


d.isupper()


# In[101]:


d.join('kill')


# In[107]:


d.ljust(25)


# In[108]:


d.lower()


# In[119]:


d.lstrip('h')


# In[128]:


d.maketrans('kill','zoom','fill')


# In[132]:


d.partition('kill')


# In[138]:


d.removeprefix('h')


# In[143]:


d.removesuffix('o')


# In[144]:


d.replace('l','g')


# In[148]:


d.rfind('l')


# In[150]:


d.rindex('l')


# In[153]:


d.rjust(20)


# In[157]:


d.rpartition('he')


# In[160]:


d.rsplit('o')


# In[163]:


d.rstrip('o')


# In[167]:


d.split('he')


# In[172]:


d.splitlines(2)


# In[176]:


d.startswith('h')


# In[178]:


d.strip('h')


# In[181]:


d.swapcase()


# In[184]:


d.title()


# In[190]:


d.translate('h')


# In[191]:


d.upper()


# In[194]:


d.zfill(20)


# In[ ]:





# **Complex**

# In[196]:


f=3+4j


# In[197]:


type(f)


# In[200]:


f.conjugate()


# In[202]:


f.real


# In[203]:


f.imag


# In[ ]:





# **Boolian**

# In[204]:


s=True


# In[205]:


type(s)


# In[206]:


s.as_integer_ratio()


# In[217]:


s.conjugate()


# In[209]:


s.bit_length()


# In[210]:


s.denominator


# In[215]:


s.from_bytes(4)


# In[219]:


s.numerator


# In[220]:


s.real


# In[221]:


s.imag


# In[225]:


s.to_bytes(10)


# In[6]:


import math as m
k=177
l=10
print(m.mod(k))
print(m.mod(l))
print(divmod(k,l))


# In[7]:


a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))

print(pow(a,b,m))


# In[10]:


thickness=int(input())
c="H"
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[11]:


i=0
while i<7:
    print("*"*i)
    i=i+1
    


# In[12]:


for i in range(1,7):
    print("*"*i)
    i+=1


# In[19]:


for _ in range(1,5+1):
    print("*"*_)
for i in range(_,0,-1):
    print("*")


# In[2]:


#extracting the matter from a html file
import re
j=open("C:/Users/chen zhen/Desktop/re_data/reddyprasad.html","r")
host=j.read()
print(host)


# In[23]:


print("The original matter is : " + str(host))
  
tag = input()
hoster = "<" + tag + ">(.*?)</" + tag + ">"
get= re.findall(hoster,host)
print("The matter extracted : " + str(get))


# In[ ]:





# In[ ]:





# In[5]:


N = int(input())
list = []
num = []
nl = []
for i in range(0,N):
    a = input()
    b = float(input())
    num.append(b)
    list.append([a,b])
#print(list)
#print(num)
num.sort()
num.reverse()
#print(num)
c = num.count(min(num))
number=num[len(num)-c-1]
#print(number)
for i in range(0,N):
    if(number==list[i][1]):
#print(list[i][0])
        nl.append(list[i][0])
        nl.sort()
#print(nl)
for x in range(len(nl)):
    print (nl[x])


# In[8]:


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    query_name = input()

    # Finding the percentage in Python - Hacker Rank Solution START
    output = list(student_marks[query_name])
    per = sum(output)/len(output)
    print("%.2f" % per)


# In[13]:


n = int(input())
marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    scores=sum(scores)/3
    marks[name] = scores
a = input()    
print('%.2f' % marks[a])


# In[14]:


regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.
# Validating Postal Codes in Python - Hacker Rank Solution END

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[15]:


import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# start   
matrix = list(zip(*matrix))

sample = str()

for words in matrix:
    for char in words:
        sample += char
       
    print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))


# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


print(map("hii",2))


# In[21]:


num1 = [4, 5, 6]
num2 = [5, 6, 7]


# In[27]:


result = map(lambda n1, n2: n1+n2, num1, num2)
print(tuple(result))


# In[41]:


class price():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print("lap top name:{0} \nLap top price:{1}".format(self.name,self.price))
        
    def Lap_det(self):
        l={"dell":25000,"dell-vostro":27000,"lenovo":35000,"lenovo-yoga":29999,"asus":40000,"dell-pevillion":45000,"asus-lima":50000,"acer-predetor":49999,"acer-300":39000}
   
        
    


# In[37]:


obj=price("dell",35000)


# In[38]:


obj.name


# In[43]:


l={"dell":25000,"dell-vostro":27000,"lenovo":35000,"lenovo-yoga":29999,"asus":40000,"dell-pevillion":45000,"asus-lima":50000,"acer-predetor":49999,"acer-300":39000}


# In[45]:


l.keys()


# In[51]:


k=int(input("enter the amount:"))
if k in l.values():
    if k<=30000:
        print(l.keys(k))


# In[59]:


j=tuple(l)


# In[63]:





# In[ ]:





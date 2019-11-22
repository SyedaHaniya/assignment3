#!/usr/bin/env python
# coding: utf-8

# In[1]:


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
add = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2
print ("Operations: \n1. Addition\n2. Subtraction\n3. Multiplacation\n4. Division")
i = input("Please select the operation(1, 2, 3, 4): ")
if i == '1':
    print(n1, "+", n2, " = ", add)
elif i == '2':
    print(n1, "-", n2, " = ", sub)
elif i == '3':
    print(n1, "*", n2, " = ", mul)
elif i == '4':
    print(n1, "/", n2, " = ", div)
else:
    print("Invalid input")


# In[2]:


my_list = ["A", "Hello", 3, "Yay", 21, 12, "H", 29]
print("Numeric values present in the list are: ")
for x in my_list:
    if type(x) == int:
        print(x)
   


# In[3]:


dic = {'a': 100, 'b': 32, 'c': 30}
print(dic)
dic['d'] = 49
dic['e'] = 12
dic['f'] = 22
dic['g'] = 51
print("After addition: ")
print(dic)


# In[4]:


dic = {'a': 10, 'b': "hello", 'c': 30, 'd': "apple", 'e': 54, 'f': 21, 'g': "mango", 'h': 24, 'i': 100}
Sum = 0
for x in dic.values():
    if type(x) == int:
        Sum = Sum + x

print(Sum)


# In[5]:


dic = {1: 10, 2: 100, 3: 10, 4: 24, 5: 54, 6: 21, 7: 14, 8: 24, 9: 100}
print("Duplicate values:")
for x in range(1, len(dic)+1):
    for y in range(x+1, len(dic)+1):
        if dic[x] == dic[y]:
            print(dic[y]);


# In[48]:


dic = {'a': 10, 'b': 12, 'c': 30, 'd': 32, 'e': 54, 'f': 21, 'g': 7, 'h': 24, 'i': 100}

k = input("Enter a new key: ")
for x in dic:
    if k in dic:
         mess = "Key already exists!!!"
    else:
        mess = "Okay"
print(mess)    


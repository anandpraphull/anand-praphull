"""print("hello")
print("8765")
a=60  ....> pre-defined 
print(a)
c="Aman"
print(c)
d=98.7
#add=a+d
#print(add)
print("enter your name ", "Anand Praphull")
print (78+49)"""
#name="Anand"
#age=26
#print(name, age)
#age2=age
#print(age2)
#print(type(name))
#print(type(age))
#nm='anand'
#nm1="ananan"
#nm3="""Anannnnd"""
#print(nm,nm1,nm3)
#salary=20000
#sal=None
#x=False
#print(salary,sal,x)
#print(type(x))
#print(type(sal))

"""d=40
e=43
sum=d+e
print(sum)
s="end "
print(6*s)
t=" never "
print(9*(s+t))"""

"""a=5
b=10
int_div=a//b
print(int_div)
a,b=3,4
c=a//b
d=a/b
print(c,d)"""
#integer division
"""a,b=-12,5
c=a//b
print(c)
#modulo/remainder
d=a%b
print(d)
a,b=-5,2
r=a%b
print(r)
#taking input from use
name = input("enter your name: ")  # it is a string type
#print(type(name))  # it show strings
print(name)
salary=int(input("write your salary: "))
print(salary)"""
"""name = input("enter your name here: ")
age = int(input("enter your age here: "))
salary = float(input("enter ypur salary: "))
print( "my name is", name, "and my age is", age, "and my salary is", salary)
# not>and>or
b=not True and False or True
print(b)"""
#conditional statement
# if-elif-else
"""age=int(input("value of age: "))
if(age>18):
    print("all is good")
elif(age<18):
    print("all not good")
else:
    print("ok")
colour=input("enter the colour: ")
if(colour=="red"):
    print("stop")
elif(colour=="green"):
    print("go")
elif(colour=="yellow"):
    print("wait")
else:
    print("colour not displaying")
year=int(input("enter the year: "))
if(year%4==0):
    print("This year is leap year")
elif(year%4!=0):
    print("this year is not leap year")"""
"""a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
calculator="+,-,*,%"
calculator=input("enter your command: ")
if(calculator=="+"):
    print(a+b)
elif(calculator=="-"):
    print(a-b)
elif(calculator=="*"):
    print(a*b)
elif(calculator=="%"):
    print(a%b)
else:
    print("This command not accepted")"""
"""marks=int(input("marks is: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("fail")"""
# single line if conditional statement or ternary operator
#<var>=<val1>if<condition>else<val2>
#name=input("enter the name: ")
#s="PM" if name=="Modi" else "CM"
#print(s)
#st1 if condition else st2
#print("A+") if name=="Anand" or name=="Mukul" else print("B+")

#clever if / ternary operator
#<var>=(false_val, true_val) [condition]  ...> if condition is true then take true value
"""sal=float(input("salary: "))
tax = sal*(0.1,0.2) [sal<=50000]
#num=int(input("enter the num value"))
#output=("odd","even") [num%2==0]
print(tax)"""
"""p=float(input("enter the principle amount: "))
r=float(input("enter rate: "))
t=float(input("enter time: "))
si=(p*r*t)/100
print(si)
a=90
b=60
c=a**b
print(c)
a="apple"
print(a in a)"""
#s="23"
'''b=int(s)......> type casting
print(b)
b +=8
print(b)'''
"""val=input("enter your nsme")
print(type(val), val)"""
"""num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
sum=num1+num2
print("sum of num1 & num2: ", sum)
s=int(input("value of side of square in meter : "))
area=s*s
print("area of square is : ", area, "metresquare") """
"""n1=float(input("enter n1 "))
n2=float(input("enter n2 "))
print("avg. eaual to ", (n1+n2)/2)"""
#n1=int(input("enter n1 : "))
#n2=int(input("enter n2 : "))
#print(True) if n1>=n2 else print(False)
#print(n1<=n2)
#strings is a datatype which stores a sequence of characters 
#strings are immutable and ordered
# str1="A"
#str2 ='b'
#str3="""c"""
#basic operation
# concatenation
#str1="hello"
#str2="world"
#print(str1+str2)
#"hello" + "world" ....> "helloworld"
#str1="this is my practice page \nhere you can find some example"   .....>escape sequence character for next line
#print(str1)

#length of string
#len(str1)
#print(len(str1))

#index of string   >>> position of str
#str1[2]
#str2[0]...>its start from 0 to n-1

#slicing in python
#str[1:3]
#str1[2:4]....>index no
#str2[1:len(str2)]
#negative index  its start from -1
#str="apple"
#str=[-1:-4]
# string function
#endwith
#str="I am an engineer"
#print(str.endswith("ne"))

#capatalise  make first letter capitals
#str="anand"
#print(str.capitalize())

#replaced(old, new)
#str1="java"
#print(str1.replace("java", "python"))

#find  character index
#print(str1.find("v"))

#count kitni bar exist kart hai
#print(str1.count("a"))
#str2=input("enter your name: ")
#print(len(str2))
#str3="strings"
#print(str3.count("s"))

#nesting   if ke andar if 
"""age=34
if(age >=18):
    if(age>=80):
        print("visibility not possoble for drive")
    else:
       print("can drive")
else:
    print("can't drive")"""
"""num=int(input("Enter the num value : "))
if((num)%2==0):
    print("even number")
else:
    print("odd number")

num2=int(input("Enter the num2 value : "))
num3=int(input("Enter the num3 value : "))
num4=int(input("Enter the num4 value : "))
if(num2>num3 and num2>num4):
    print("num2 is greates no")
elif(num3>num2 and num3>num4):
    print("num3 is greates no")
else:
    print("num4 is greatest no")
num5=int(input("Enter the num5 value : "))
if(num5%7==0):
    print("num5 is multiple of 7")
else:
    print("num5 is not multiple of 7")"""

#list
# A list in Python is a collection of items which is ordered and mutable (can be changed).
# Lists can contain elements of different data types (integers, strings, floats, etc.).
# Lists are defined using square brackets [].

# Example:
#my_list = [1, 2, 3, "apple", 4.5]
#print(my_list)

# Accessing elements:
#print(my_list[0])  # prints 1
#print(my_list[3])  # prints "apple"

# Modifying elements:
#my_list[1] = "banana"
#print(my_list)

# Adding elements:
#my_list.append("new item")
#print(my_list)

# Removing elements:
#my_list.remove(3)
#print(my_list)

# List length:
#print(len(my_list))

"""my_list2=["anand","mohan",23,45,98.4]
print(type(my_list2))
print(my_list2[4])
print(len(my_list2))"""
"""#slicing in list
student=[1,100,50,500,60]
#print(student)
#print(student[1:4])

#method in list
#append  add one element in the end
student.append(55)
print(student)

#sort  sorts in ascending order
print(student.sort())  #here return none
print(student)
print(student.sort(reverse=True))  #reverse in decending inoriginal list
print(student)
str1=["amam","zyss","huyt"]
print(str1.sort())
print(str1)

#insert similar to append but it add at particular index
student.insert(2,68)
print(student)

#remove it remove first occurence of element
str2=[2,1,3,4,1]
str2.remove(1)
print(str2)

#pop remove element at index
str2.pop(3)
print(str2)"""


#tuple it like string immutuable
#it created with ()
"""str3=(1,4,5,7)
print(type(str3))
print(str3)
print(str3.index(5))
print(str3.count(4))"""
"""str4=(2,)    #  it is slightly different to str4=(2) its is int type but (2,) is tuple type
print(type(str4))
print(str4)
movie_list=[]
movie_list1=input("enter your fav movie1: ")
movie_list2=input("enter your fav movie2: ")
movie_list3=input("enter your fav movie3: ")
movie_list.append(movie_list1)
movie_list.append(movie_list2)
movie_list.append(movie_list3)
print(movie_list)"""

#movie_list.append(input("enter your movie"))   directly add karne ke liye
"""list=[]
list=input("enter list here")

if(list==list[::-1]):
    print("polindrone")
else:
    print("not polindrome")"""
"""str1=[1,2,3,2,1]
str2=str1.copy()
if(str1==str2.reverse()):
    print("polindrome")
else:
    print("not polindrome")"""

# dictionary  {}
"""my_dict={"name":"anand"}
print(my_dict)
my_dict={
        "age":24,
        "height":168,
        "adult":True
        }
print(my_dict)
print(my_dict["height"])
my_dict["salary"]=80000
print(my_dict)
print(my_dict["salary"])
my_dict["mobilenumber"]=8566872176
print(my_dict)
my_dict["name"]="Anand"
print(my_dict)
my_dic2={}
print(my_dic2)

##nested dictionary  for this kisi key value ko dictionary bna skte hai
Employee={
         "name":"Aman",
         "Bank":{
             "sbi":7888775,
             "pnb":90876666,
             "icici":889876754
         },
         "salary":45000,
         "unit":"rcladm"
}
print(Employee)
print(Employee["Bank"]["pnb"])
# dictionary method
print(list(Employee.keys()))
print(len(Employee))
print(Employee.keys())    #retirn all keys
print(Employee.values())   #return all values
print(Employee.items())     #return all (key value) pairs as tuples
print(Employee.get("unit"))   #return the key according to value
#print(Employee["unit2"])  # return error 
#print(Employee.get("unit2"))   #return none
Employee.update({"unit":"Engg"})
print(Employee)
Employee.update(my_dict)
print(Employee)


my_name="Anand"  #string
my_name=["Anand","Praphull"]  #list
my_name=(1,2,3,4,"anand")  #touple
#my_name={                  # dictionary
    #"name":"Anand",
    #"age":25
#}
print(my_name)

print(f"my tuple is {my_name}")
name="you"
age=78
print(f"my name is {name} and my age is {age}")

n1=int(input("enter n1"))
n2=int(input("enter n2"))
for num in range(n1,n2):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
         print(num)"""

            
        
##set collection of unordered items
#each element in set is unique
#int,float,string,boolean, tuple are stored in set
#list,dictionary can't be stored in set because these both are mutable and set is immutable
"""nums={1,2,3,4,2,5}
print(nums)
collection ={"shirt","jeans","coat","paint"}
print(type(collection))
print(len(collection))
print(collection)

collection2={1,2,2,5,"Anand",5,6,"Aman"}
print(collection2)
collection3=set()
print(type(collection3))

#set methods
collection3.add(2)  #add method
print(collection3)
collection2.remove(1)   #remove method
print(collection2)  #set is mutable but elements are immutable
collection.clear()
print(collection)
print(collection2.pop())
print(collection2.pop())  # it will choose random value
print(collection2)

print(collection2.union(collection3))

set1={1,2,3,4,5}
set2={6,7,8,9,2,1,0}
print(set1.union(set2))  #combines both set and return new  set with unique value
print(set2.intersection(set1))  #combines comman value and return new value
dict1={"table":("a piece of furniture","lists of facts & fugure"),"cat":"a small animal"}
print(dict1)

classroom={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(classroom))

dict2={}
dict2["math"]=90   #adding value to dictionary
dict2["science"]=89
dict2["sst"]=87
print(dict2)
value=int(input("enter your marks'value : "))
dict2.update({"his":value})
value=int(input("enter your marks'value : "))
dict2.update({"geo":value})
value=int(input("enter your marks'value : "))
dict2.update({"commerce":value})
print(dict2)

set5={9,"9.0"}
set5={
    ("int",9),
    ("float",9.0)
}
print(set5)"""

#num=int(input("enter the num value"))
#output=("odd","even") [num%2==0]  #false value, true value if ([] this 
#bracket condition is true then return true value otherwise false value return
#print(output)

#a="apple"
#print(a in a)  #return true

"""i=1    #i is iterator and this is iteration operation
while i<=100:
    print(i)
    i+=1
print(i) """ #it will give last value of i

"""num=int(input("enter the value of num : "))
i=1
while i<=10:
    print(num*i)
    i+=1

list1=[1,4,9,16,25,36,49,64,81,100]  # traverse going to each element in list
x=49
i=0
while i<len(list1):
    print(list1[i])
    if (list1[i]== x):
        print("found on ", i,"th index",x)
    i+=1"""

"""tup1=(1,4,9,16,25,36,49,64,81,100)
print(tup1[1])

# break ...> loop wahi pe terminate ho jayega
x=36
i=0
while i<len(tup1):
    print(tup1[i])
    if (tup1[i]==x):
        break
    i+=1

#continue ...> current iteration ko terminate karta hai
#  aur uske bad fir continue karta hai
i=0
while i<6:
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if (i%2==0):
        i+=1
        continue
    print(i)
    i+=1"""
# for loop  used for sequencial traversal. for traversing list, string, tuples etc.
# for iteration we used while and for traversing we used for
"""list2=[1,2,3,4,5,6,7,"Anand"]
for val in list2:
    print(val)
tup=(3,5,7,9,10)
for element in tup:
    print(element)
strr="ro","ko","hi"
for st in strr:
    print(st)

for char in strr:
    print(char)
stt="aappllee"
for e in stt:
    if(e=="d"):
        print("ok got it")
        break
    print(e)
else:
    print("complete")

num=int(input("Enter number here : "))
for n in range(2,num):
    if(num%n==0):
        print("not prime no")
        break
    print(n)
else:                         #optional if in for loop
    print("prime no")
listt=[1,4,9,16,25,36,49,64,81,100]
for i in range(0,len(listt)-1):
    print(listt[i])
    if(listt[i]==64):
        print("ok got it",i)
        break
else:
    print("not found")"""


"""lis=[1,4,9,16,25,36,49,64,81,100]
x=81
idx=0
for ell in lis:
    print(ell)
    if (ell==81):
        print("found in list ",idx)   #linear search
    idx+=1"""

#range  (start value, stop value, step size)
# step size default value is 1
#range(5)  it means it start default from 0 and to 5(end before 5)

"""print(range(5))
seq=range(6)
for i in seq:
    print(i)
for i in range(2,10,2):  # even number 
    print(i)"""

##for i in range(1,101,1):
    ##print(i)
#for i in range(100,0,-1):
    #print(i)
#n=int(input("enter n value : "))
#for i in range(n,11*n,n):
   # print(i)

#pass statement  null statement placeholder for future code
#for i in range(1,6,2):
    #pass
#print("pass statement")

#sum of first n number by using while loop
n=int(input("enter n here : "))
i=1
sum=0
while i<=n:
    sum += i
    i+=1
print("sum of first",n ,"natural number is", sum)

# factorial of n number

n=int(input("type n value here : "))
fact=1
for i in range(1,n+1):
    fact *= i
    
print("fatorial of first", n, "number is ", fact)

n=int(input("n value : "))
fact1=1
i=1
while i<=n:
    fact1 *= i
    i+=1
print(fact1)


    






# 1 write a python function to check the given number is even or odd

'''n=eval(input('enter any number:'))

def evenorodd(n):
    if n%2==0:
        print(n,'is a even number')

    else:
        print(n,'is a odd number')

evenorodd(n)'''

#2 write a python function to check the given number is positive or negative

'''n=eval(input('enter any number:'))

def psgorneg(n):
    if n>0:
        print(n,'is a positive number')

    else:
        print(n,'is a negative number')

psgorneg(n)'''

#3 write a python function to check the given number is divisible by 10 or not

'''n=eval(input('enter any number:'))

def divby10(n):
    if n%10==0:
        print(n,'is divisible by 10')

    else:
        print(n,'is not divisible by 10')

divby10(n)
'''

# 4 write a python function to print first n even numbers
'''n=eval(input('enter any number:'))
lst=[]
def neven(n):
    for i in range(1000):
        if i %2==0:
            lst.append(i)
        if len(lst)==n:
            break
    print(lst)

neven(n)

'''

# 5 write a python function to print first n odd numbers
'''n=eval(input('enter any  number:'))
lst=[]
def nodd(n):
    for i in range(1000):
        if i%2!=0:
            lst.append(i)
        if len(lst)==n:
            break
    print(lst)
nodd(n)'''

# 6 write a python function to print even numbers upto n

'''n=eval(input('enter any number:'))
def evenupton(n):
    for i in range(n+1):
        if i%2==0:
            print(i)
evenupton(n)'''

# 7 write a python function to print odd numbers upto n
'''n=eval(input('enter any number:'))
def oddupton(n):
    for i in range(n+1):
        
        if i%2!=0:
            print(i)

oddupton(n)'''

#8 write a python function to print sum of digits of n
'''n=eval(input('enter any number:'))
def sumofdigits(n):
    s=0
    for i in range(n+1):
        s=s+i
    print(s)
sumofdigits(n)'''

# 9 write a python function to print the three  largest number of given values
'''n1=eval(input('enter first number:'))
n2=eval(input('enter second number:'))
n3=eval(input('enter third number:'))

def largestnumber(a,b,c):
    if a>b and a>c:
        print(a,'is the largest number of ',b ,'and', c)

    elif b>c:
        print(b,'is the largest number of ',a, 'and' ,c)
    else:
        print(c,'is the largest number of ',a ,'and' ,b)

largestnumber(n1,n2,n3)
'''

#10 write a python function to reverse the given number of string
'''n=input('enter a string or number:')
def reversestring(s):
    
    st1=s[::-1]
    print(st1)
reversestring(n)'''

#or
'''n=input('enter a string or number:')
def reversestring(s):
    
    st1=''.join(reversed(s))
    print(st1)
reversestring(n)
'''
#11 write a python function to print the factors of given number
'''
n=eval(input('enter any number:'))
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
factors(n)'''
#12 write a python function to print the factorial of given number
'''n=eval(input('enter any number:'))

def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print(s)
factorial(n)'''

#13 write a python function to swap the two given numbers
'''n1=eval(input('enter first number:'))
n2=eval(input('enter second number:'))

def swap(x,y):
    temp=x
    x=y
    y=temp
    print('first number',n1,'after swapping',x)
    print('second number',n2,'after swapping',y)

swap(n1,n2)'''
#14 write a python function to check the given number is prime or not
'''n=eval(input('enter any number:'))
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,'is not prime')
            break
    else:
        print(n,'is  prime')
prime(n)'''

#15 write a python function to check the given number is palindrom  or not
n=eval(input('enter any number:'))
def palindrome(num):
    if num==str(num)[::-1]:
        print(num,'palindrome number')
    else:
         print(num,'not a palindrome number')
palindrome(n)





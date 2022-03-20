"""
a =1
b = 2
c = 3

print(a == b)
print(a + b)
print(a * b)


# if condition

condition = True

if condition:
    print('do if')
    print('do lf')
    print('do ef')
    print('do tf')
else:
    print('do ttt')
"""

#
##if user_account =='qzl' and user_password == '123456':
##    print('login success')
##else:
##    print('please chack your account or password')

##if user_account != account:
##    print("user erros!")
##elif user_password != password:
##    print("password errors!")
##else:
##    print("login successsss")

##
##if user_account == account:
##    if user_password == password:
##        print("login success")
##    else:
##        print("errors password")
##else:
##    print("error account!")
## while 不知道循环多少次 无法确定次数
##condition = True
##while condition:
##    print('hello world')

##x = 1
##while x <= 10:
##    print(x)
##    x += 1
##else:
##    print('else',x)

##for 遍历

##for ---  in --:
##    #---
##    
##sequences = [['red','blue','green','yellow','orange'],[1,2,3]]
##for i in sequences:
##    for y in i:
##             print(y)
##count = 0
##colors = ['red','blue','green','yellow','orange']
##for color in colors:
##    print(color)
##    count += 1
##else:
##    print('else',count)

##break continue
"""
count = 0
colors = ['red','blue','green','yellow','orange']
for color in colors:
    if color == 'yellow':
        break
    print(color)
    count += 1
else:
    print('else',count)


count = 0
colors = ['red','blue','green','yellow','orange']
for color in colors:
    if color == 'yellow':
        continue
    print(color)
    count += 1
else:
    print('else',count)
"""
##for(i=1;i<=10;i++)

##for i in range(1,10,2):
##    print(i)
##for i in range(9,0,-2):
##    print(i)

##a = [1,2,3,4,5,6,7,8,9,10]
##for i in a:
##    if i % 2 == 0:
##        continue
##    print (i,end='|')
a = [1,2,3,4,5,6,7,8,9,10]
##for index in range(0,10,2):
##    print(a[index],end = '|')
##print(a[::2])
for i in a[::2]:
    print(i)

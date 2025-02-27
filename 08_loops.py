print("----------for condition--------")
for i in range(5):
    print(i)
print("--------------------------------")
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print("------while condition---------")
#1.initilization 
#2.condition
#3.itration/incrament-decrement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
#continue        
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number:",num)
        continue
    print("Found an odd number:",num)
#starting point->ending point->increment
for i in range(0,16,4):
    print("HELO",i)
#--------counetr controlled loop---------
#1.initilization
#2.condition
#3.itration
import random
x= input ( "ali rolled:")
y= input ( "ahmad rolled:")
player1=0
player2=0
for i in range(1,6):
    n= random.randint(1,6)
    print(x,"rolled",n)
    player1=player1+n
    m= random.randint(1,6)
    print(y,"rolled",m)
    player2=player2+m
if player1>player2:
    print(x,"wins")
elif player2>player1:
    print(y,"wins")
else:
    print("draw")
print("score of",x,"is",player1)
print("score of",y,"is",player2)
#--------sentinel controlled loop---------
print("------sentinel controlled loop-------")


#2
print('Hello World')
#3
print('sun 10225501459')

#4
for i in range(0,10):
    print(chr(0x2605),end='')
print('\n')

print(chr(0x2605),end='')
print('dase intro',end='')
print(chr(0x2605))
for i in range(0,10):
    print(chr(0x2605),end='')
print('\n')
#5
a =int(input('enter a'))
b =int(input('enter b'))
c =int(input('enter c'))
li=[]
li.append(a)
li.append(b)
li.append(c)
li.sort(reverse=True)
print(li)
#6
a =int(input('enter a'))
b =int(input('enter b'))
c =int(input('enter c'))
d=int(input('enter d'))

li2=[]
li2.append(a)
li2.append(b)
li2.append(c)
li2.append(d)
li2.sort(reverse=False)
print(li2)

#7
for i in range(1,100,2):
    print(i,end=' ')

#8
summ=0
for i in range(1,101):
    summ+=i
print(summ)
#9
L=input('输入LIST').split() 
L.reverse()       
leng=len(L)
for i in range(0,leng):    
    print(L[i])

k=0
while(k<=leng-1):
    print(L[k])
    k+=1
#10
S=input('输入S')
S=list(S)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
print(S)

for i in range(0,len(S)-1):
    if(S[i]==S[i+1]):
        print("YES")
        break
#11
SS=input('输入SS').replace(' ','')
print(SS)
#12
def cubic_root(n, epsilon=1e-6):
    if n < 0:
        raise ValueError("无法对负数取3次方根")

    low = 0
    high = max(1, n)  

    while True:
        guess = (low + high) / 2 
        error = guess**3 - n 

        if abs(error) < epsilon:  
            return guess

        if error < 0:
            low = guess  
        else:
            high = guess  
print(cubic_root(n=3.1415926))
#13
def factorial(a):
    fc=1
    for i in range(1,a-1):
        fc=fc*i
    return fc
print(factorial(9))
    

                                                                                                                                   

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

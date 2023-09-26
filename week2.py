import random
import math
import networkx as nw

#第一题
def dp_maxlist(n):
    L=[0]*(n+1)
    R=[[]for i in range(0,n+1)]
    R[1]=[1]
    L[1]=1
    for i in range(2,n+1):
        L[i]=i
        R[i]=[i]
        for j in range(1,i+1):
            if(L[i]<L[j]*L[i-j]):
                R[i]=R[j]+R[i-j]
            L[i]=max(L[i],L[j]*L[i-j])
    print(R[n])
    return L[n]

print(dp_maxlist(3))

#第二题
for i in range(10,60,10):
    print("2**"+str(i)+"="+str(2**i))

#第三题
G=nw.Graph()
G.add_nodes_from(['PSWV','WV','PWV','W','PSW','V','PSV','S','PS','win'])
G.add_edges_from([('PSWV','WV'),('PWV','WV'),('PWV','W'),('W','PSW'),('PWV','V'),('PSW','S'),('PSV','V'),('PSV','S'),('S','PS'),('PS','win')])
print('可行方法有：')
print(list(nw.all_simple_paths(G=G,source='PSWV',target='win')))
#第四题
c=2
g=0
step=0.0001
e=0.0001
for g in range(0,c+1):
    if(g*g>c):
        g=g-1
while(abs(g*g-c)>e):
    g=g+step
print(g)

#第五题 第六题
SQU=8
ans=SQU/2
err=0.000001
COUNT=0
while(abs(ans*ans-SQU)>err):
    ans=(ans+SQU/ans)/2
    COUNT=COUNT+1
print(ans)
print(COUNT)

#第七题
#计算得到g=c/3g^2+2g/3
SQU2=8
ans2=SQU2/2
err2=0.000001
COUNT2=0
while(abs(ans2*ans2-SQU2)>err):
    ans2=SQU2/(3*ans2*ans2)+2*ans2/3
    COUNT2=COUNT2+1
print(ans2)
print(COUNT2)

#第八题

sumall=10000
count=0
for i in range(sumall):
    a=random.uniform(0,1)
    b=random.uniform(0,1)
    d_=a*a+b*b
    if(d_<=1):
        count=count+1
pai=(count/sumall)*4
print("圆周率 蒙特卡洛：{:.10f}".format(pai))

pai2=0
for n in range(10000):
    pai2=pai2+pow(-1,n)*1/(2*n+1)
pai2=4*pai2
print("圆周率 反正切级数：{:.10f}".format(pai2))

pai3=0
N=10000
half_angle=math.pi/N
S3=N*math.sin(half_angle)*math.cos(half_angle)
print("圆周率 多边形近似：{:.10f}".format(S3))
#N边形面积，即近似园面积



#第九题
Sumall=10000
Count=0
for i in range (Sumall):
    X=random.uniform(2,3)
    Y=random.uniform(0,21)
    if(Y<pow(X,2)+4*X*math.sin(X)):
        Count=Count+1
S=(Count/Sumall)*21
print("积分值："+str(S))



        




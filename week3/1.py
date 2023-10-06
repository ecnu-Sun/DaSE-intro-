#第一题
N=123.456
INT=bin(int(N))
DECI=N-int(N)
BI_DECI=''
count=0
while(DECI>0 and count<15):
    BI_DECI=BI_DECI+str(int(DECI*2))
    DECI=DECI*2-int(DECI*2)
    count=count+1
print(str(N)+'='+str(INT)+'.'+BI_DECI)

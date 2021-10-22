seq1=[1,2,3,4,5,6,7,8,9,10]
seq2=[1,2,3,4,5,6,7,8,9,10]
vaium=[0,0,0,0,0,0,0,0,0,0,0]
resp=[0,0,0,0,0,0,0,0,0,0,0]
a = len(seq1)
for(i) in range(a,0,-1):
    vaium[i-1]=(seq1[i-1]+seq2[i-1])//10
#if (seq1[i-1]+seq2[i-1]+vaium[i])>9):
 #   resp[i]=(seq1[])

print(vaium)
print(seq1)
print(seq2)
print(resp)

seq1=[1,2,3,4,5,6,7,8,9,10]
seq2=[1,2,3,4,5,6,7,8,9,10]
vaium=[0,0,0,0,0,0,0,0,0,0,0]
resp=[0,0,0,0,0,0,0,0,0,0,0]
a = len(seq1)
for(i) in range(a,-1,-1):
    vaium.insert(0,(seq1[i] + seq2[i])//10)
    resp.insert(0,((seq1[i]+seq2[i])%10))


print(vaium)
print(seq1)
print(seq2)
print(resp)


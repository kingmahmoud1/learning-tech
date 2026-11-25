num="011010111010110"
m=len(num)
tot=0
for (n,i) in enumerate(num):
    b=int(i)
    if b==0:
        continue
    else :
       tot=tot+2**(m-1-n)

print(tot)
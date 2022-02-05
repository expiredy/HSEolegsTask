A = [0, -4, 1, 5,  -4, 5]
rez_i = 0
for i in range(1, len(A)):
    if A[i]<A[rez_i] :  
        rez_i = i

print(rez_i)
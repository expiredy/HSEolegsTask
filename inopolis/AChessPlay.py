n = int(input())
m = input().split()
answer = m
for i in range(n):
    m[i] = (int(m[i]), i)
s = sorted(m, reverse=True)
a = 0
b = 0
for i in range(n):
    if a >= b:
        b += s[i][0]
        answer[s[i][1]] = 1
    else:
        a += s[i][0]
        answer[s[i][1]] = 2
print(abs(a-b))
print(*answer)
srt1 = input()
num = {}

for i in range(len(srt1)):
    j = srt1[i]
    if j in num:
        num[j] += 1
    else:
        num[j] = 1

print(num)

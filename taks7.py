num = int(input())
a = 2 * num - 1

for i in range(1, a + 1):
    if i <= num:
        j = i
    else:
        j = 2 * num - i
    for j in range(j):
        print("*", end=" ")
    print()

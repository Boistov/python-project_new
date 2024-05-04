# Given string
text = input()
n = "Emma"

num = 0

for i in range(len(text) - len(n) + 1):
    if text[i:i+len(n)] == n:
        num += 1

print(num)

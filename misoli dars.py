sentence = input().split()
symbol = input()
counter = 0


for i in range(len(sentence) - len(symbol) + 1):
    if sentence[i:i + len(symbol)] == symbol:
        counter += 1
print(counter)







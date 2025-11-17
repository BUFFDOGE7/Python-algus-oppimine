
n = int(input("Enter an integer between 1 and 9: "))

nn = n
for i in range(9):
    nn += n

nnn = n
for i in range(9):
    nnn += n
for i in range(9):
    nnn += nn

result = n + nn + nnn

print(f"{n} + {nn} + {nnn} = {result}")
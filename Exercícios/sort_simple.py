values = input().split()

for i in range(3):
    values[i] = int (values[i])
values2 = sorted(values.copy())

for i in range(3):
    print(values2[i])
print()
for i in range(3):
    print(values[i])
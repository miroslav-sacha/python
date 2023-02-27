set1 = ["🟥", "🟥", "🟥"]
set2 = ["🟥", "🟥", "🟥"]
set3 = ["🟥", "🟥", "🟥"]
all_sets = [set1, set2, set3]
print(f"{set1}\n{set2}\n{set3}")
position = input("Zadejte souradnice")

num1 = int(position[0])
num2 = int(position[1])

print(num1)
print(num2)


all_sets[num1][num2] = "X"

print(f"{set1}\n{set2}\n{set3}")
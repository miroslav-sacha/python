import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

print("New password !!!")

num_letters = int(input("Kolik pismen chcete: \n"))
num_numbers = int(input("Kolik cisel chcete: \n"))
num_special_char = int(input("Kolik spec. znaku chcete: \n"))

result = []
for index in range(0, num_letters):
    random_number = random.randint(0, len(letters)-1)
    result.append(letters[random_number])

for index in range(0, num_special_char):
    random_number = random.randint(0, len(special_char)-1)
    result.append(special_char[random_number])

for index in range(0, num_numbers):
    random_number = random.randint(0, len(numbers)-1)
    result.append(numbers[random_number])
print(result)
# preskupeni
# translator = ""
# for index in range(0, 10):
#     random_index_1 = random.randint(0, len(result)-1)
#     random_index_2 = random.randint(0, len(result)-1)

#     translator = result[random_index_2]
#     result[random_index_2] = result[random_index_1]
#     result[random_index_1] = translator

random.shuffle(result)

print(result)

# # prevod listu na string
result_password = ""

for one_character in result:
    result_password += one_character

print(f"Vase nove heslo je: {result_password}")
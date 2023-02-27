alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode (message, shift_number):
    shifted_text = ""
    for one_letter in message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index + shift_number
            shifted_text += alphabet[new_index]
        else:
            shifted_text += one_letter
    print(f"Váš zakodovany text je: {shifted_text}")

encode ("davide ahojky", 5)

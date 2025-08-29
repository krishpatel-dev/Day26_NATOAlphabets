import pandas

data = nato_list = pandas.read_csv("nato_phonetic_alphabet.csv")

#print(data.to_dict())
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()

# is_continue = True
# while is_continue:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print(output_list)
#         is_continue = False
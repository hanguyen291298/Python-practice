import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_data)

your_input = input("Enter your input: ")
output = [dict_data[letter] for letter in your_input.upper() if letter in dict_data]
print(output)
import pandas

nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input('Enter the Word: ').upper()
list_words = [new_dict.get(item) for item in word.strip()]
print(list_words)

with open('./Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()
with open('./Input/Letters/starting_letter.txt') as starting_letter_file:
    starting_letter_text = starting_letter_file.read()
    for name in names:
        name = name.strip()
        letter = starting_letter_text.replace("[name]", name)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w+') as file:
            file.write(letter)
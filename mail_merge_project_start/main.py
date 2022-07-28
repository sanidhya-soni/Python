#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# list_names = []

with open('./Input/Names/invited_names.txt', mode='r') as names:
    list_names = names.readlines()

for i in range(0, len(list_names)):
    list_names[i] = list_names[i].strip()

with open('./Input/Letters/starting_letter.txt', mode='r') as content:
    text = content.read()

for i in list_names:
    path = f'./Output/ReadyToSend/letter_to_{i}.txt'
    with open(path, mode='w') as letter:
        content = text.replace('[name]', i)
        letter.write(content)

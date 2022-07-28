# In the code below, we don't need to close the file
# with open('My_Text.txt') as file:
#     contents = file.read()
#     print(contents)

# OR
# file = open('My_Text.txt')
# contents = file.read()
# print(contents)
# file.close()

# In the case shown above we need to close the file while in the 1st case we don't need to close the file.

# with open('My_Text.txt', mode='w') as file:         # Opening file in write mode
#     file.write('Cleared and Written\n')
#
# with open('My_Text.txt', mode='a') as file:         # Opening file in append mode
#     file.write('Appended Text\n')

with open('../mini-projects/My_Txt.txt', mode='r+') as file:
    content = file.read()
    print(content)

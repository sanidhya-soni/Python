with open("./deys-sir/My_File.txt", 'a') as file:
    file.write("\nWritten")
    # contents = file.read()
    # print(contents)

with open("./deys-sir/My_File.txt", 'r') as file:
    contents = file.read()
    print(contents)
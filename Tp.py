row1 = ["😁", "😅", "😂"]
row2 = ["❤", "🤣", "😍"]
row3 = ["😎", "😊", "🙄"]
emoji = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

emoji[2][1] = 3
print(f"{row1}\n{row2}\n{row3}")

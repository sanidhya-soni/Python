import replit

bidding = True
bids = {}

while bidding:
    name = input("Enter Your Name: ")
    bids[name] = int(input("Your Bid: "))
    x = input("Type 'Yes' for more bids and 'No' to stop bidding: ")
    replit.clear()
    if x != "Yes":
        bidding = False

maximum = 0
for i in bids:
    if bids[i] > maximum:
        name = i
        maximum = bids[i]

print(f"\n\nMax Bid was of ${maximum} made by {name}")

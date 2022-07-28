# Creating Dictionary
dic = {1: 2, 4: 7}
print(dic[4])

# Adding items in dictionary or editing an existing value......
# If the key is already present then it will edit
# else it will create a new entry and add the value
dic["H"] = 87
print(dic["H"])

# Printing Complete Dictionary
print(dic)

# Looping in a dictionary
for i in dic:
    print(i)  # This prints only key
    print(dic[i])  # This prints value of that key

# Wiping an existing dictionary
dic = {}
print(dic)

# Nesting a list in a dictionary
cars = {"Audi": ["A6", "RS", "Q8"],
        "Mercedes": ["Maybach GLS 600", "S-Class", "E-Class"],
        "BMW": ["X7", "5 Series"]}

for i in cars:
    print(f"{i} : {cars[i]}")

# Nesting dictionary in a dictionary
continents = {
    "Asia": {"Countries": ["India", "Sri Lanka", "Bangladesh", "Pakistan"],
             "Total_Visits": 10},
    "America": {"Countries": ["Canada", "Brazil", "Cuba"],
                "Total_Visits": 0},
    "Europe": {"Countries": ["Germany", "France", "Italy"],
               "Total_Visits": 18}}

# Nesting dictionaries inside a list
cartoons = [
    {"Tom and Jerry": ["Tom", "Jerry", "Spike", "Son of Spike", "Duckling"]},
    {"Oggy and the Cockroaches": ["Oggy", "Jack", "Joey", "Dee-Dee", "Marky"]}
]

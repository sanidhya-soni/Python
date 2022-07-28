class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("User has been created !")


    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = 10          # This is another way to define attributes of a class.
# user_1.name = 'sani'
# user_2 = User()
# user_2.id = 20
# user_name = 'priya'
# user_3 = User()
# print(user_2.id)

user_1 = User(10, 'sani')
user_2 = User(20, 'priya')
print(user_1.username)
user_2.ide = 200
print(user_2.ide)

user_1.follow(user_2)       # User 1 follows user 2
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

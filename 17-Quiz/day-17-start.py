# PascalCase - used to name classes mostly
# camelCase - used not so much
# snake_case - used to name most things in python

class User:

    # initialise attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Allan")  # (An object created from the class User)
user2 = User("002", "Maurine")
user1.follow(user2)
print(user1.followers)
print(user1.following)


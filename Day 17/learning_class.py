# Learning how to make a class
class User:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        # To provide default attribute
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("01", "Jack")
user_2 = User("02", "Angela")

user_2.follow(user_1)
print(user_1.followers)
print(user_2.following)

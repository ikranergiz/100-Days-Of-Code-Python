class User:  # PascalCase #snake_case

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user1 = User("001", "ikra")
user2 = User("002","angela")

user1.follow(user2)

print(user1.followers)
print(user2.followers)

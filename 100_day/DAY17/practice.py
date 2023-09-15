class insta:
    def __init__(self,user_id, username):
        self.username = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user1 = insta(23,"Jacxx")
user2 = insta(32,"dqsa")

print(user1.followers,user1.following)
print(user2.followers,user2.following)
print("---------------------------------")
user1.follow(user2)
print(user1.followers,user1.following)
print(user2.followers,user2.following)

# now we know how to create class , attributes,methods
from user import User

peter = User("Peter", "Get12345")
print("Hashed password: {}".format(peter._hashed_password))
print("Hashed password: {}".format(peter._hashed_password))
peter.password = "Set12345"
print("Hashed password: {}".format(peter._hashed_password))
print("Salt: {}".format(peter.salt))
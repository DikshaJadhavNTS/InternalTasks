
UserName={'Mrunal':'xyz', 'Diksha':'pqrs', 'Preti':'abcd'}


u = input("Enter username: ")
p = input("Enter password: ")


if u in UserName and UserName[u] == p:
    print(" Authentication successful")
else:
    print(" Authentication failed!")

# def authenticate(username, password):
#     for i in range(len(UserName)):
#         if UserName[i] == username and Password[i] == password:
#             return True
#     return False

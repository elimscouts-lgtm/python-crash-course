users = ()
if users:
    for user in users:
        if user == "admin": print("Hello admin, would you like to see a status report?")
        else: print(f"Hello, {user.title()}, what would you like to do today?")
else: print("We need some users!")

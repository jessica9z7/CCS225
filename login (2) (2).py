# Jessica Kusmierz
# CSS-225
# 11/28/2025

#!/usr/bin/env python
username = input("Login: >> ")
# Line 2 shows the Login on the screen
user1 = "Jack"
# Line 4 is the username
user2 = "Jill"
# Line 6 is the second username
if username == user1:
# Line 8 checks if the username and user1 are the same
    print("Access granted")
# Line 10 lets you in if the username is correct
elif username == user2:
    print("Welcome to the system")
# Line 13 welcomes you to the system if checked that evrything is True
else:
    print("Access denied")
# Line 16 does not let you keep going since the username is not correct
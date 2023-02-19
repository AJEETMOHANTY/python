# To check the format of the email.
email = input("enter the email address")
if "@" in email:
    password = input("password")

    if email == "ajeetmohanty2004@gmail.com" and password == "12345":
        print("welcome")
    elif email == "ajeetmohanty2004@gmail.com" and password != "12345":
        print("incorrect password")
        password = input("type your password again")
        if (password == "12345"):
            print("welcome")
        else:
            print("still incorrect password")
    else:
        print("incorrect credential")
else:
    print("incorrect email id")

"""
# To check the entered email is correct but password was incorrect.

email = input("enter the email address")
password = input("password")
if email=="ajeetmohanty2004@gmail.com" and password=="12345":
    print("welcome")
elif email=="ajeetmohanty2004@gmail.com" and password!="12345":
    print("incorrect password")
    password = input("type your password again")
    if(password=="12345"):
        print("welcome")
    else:
        print("still incorrect password")
else:
    print("incorrect credential")

"""
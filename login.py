import re

class User:

    def __init__(self, userId, email, password):
        self.userID = userId
        self.email = email
        self.password = password

    def validate_email(self):
        reg_ex = r'\b[A-Za-z0-9]+@+[a-z]+\.[A-Z|a-z]{2,}\b'
        if re.match(reg_ex, self.email):
            return True
        else:
            print("Enter a valid email adress")
            return False

    def check_password(self):
        if len(self.password) < 8 or self.password.isalpha():
            print("Enter a alphanumeric password")
            return False
        if(re.search("[A-Za-z]",self.password) and re.search("[0-9]",self.password) and re.search("[_@$]",self.password)):
            return True


    def validate_password(self, password):
        if self.password == password:
            print("Authorization Accepted!")
            return True
        else:
            print("wrong Password")
            return False


def validate_user(User, password):
    if User.validate_email() and User.validate_password(password) and User.check_password():
        return True
    else:
        return False


v = User(1, "hello@gmail.com", "abc@123_")

if validate_user(v,"abc@123_"):
    print("Logging In!")
else:
    print("Error Occured!")

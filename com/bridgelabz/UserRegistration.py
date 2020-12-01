
import re

class UserRegistration:


    # User First Name
    def userfirstname(self):

        pattern1 = '^[A-Z]{1}[a-z]{3,}$'
        user_name = input("Enter the User First Name : ");
        result = re.match(pattern1,user_name)
        if result:
         print("Valid Name")

        else:
                print("Invalid input, Please enter the valid name")

     #User LastName

    def userlastname(self):
        pattern2 = '^[a-z]{3,}[A-Z]{1}$'
        user_name = input("Enter the User Last Name : ")
        result = re.match(pattern2, user_name)
        if result:
            print("Valid Name")

        else:
            print("Invalid Name, Please enter proper name")

 # User Email
    def user_email(self):
        pattern3= '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2})*$'
        user_email = input("Enter the Email Id : ")
        if re.fullmatch(pattern3, user_email):
         print("Valid Email Id")

        else:
          print("Invalid Emaild Id")



if __name__ == "__main__":
    user = UserRegistration()
    user.userfirstname()
    user.userlastname()
    user.user_email()

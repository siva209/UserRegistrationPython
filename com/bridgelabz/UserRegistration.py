
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

if __name__ == "__main__":
    user = UserRegistration()
    user.userfirstname()

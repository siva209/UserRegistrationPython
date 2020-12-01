
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

     #User MobileNumber

    def usermobilenumber(self):

        patern4= '^[91]{2}[ ]?[0-9]{10}$'
        usermobnumber = input("Enter the Mobile Number : ")
        if re.fullmatch(patern4, usermobnumber):
            print("Valid Mobile Number")

        else:
            print("Invalid Mobile Number")

    # User password Rule 1

    def userpassword(self):

    #Passeword should be minimum 8 characters
        pattern5='^[a-zA-Z]{8,}$'
        userpassword = input("Enter the Password : ")
        if re.fullmatch( pattern5, userpassword):
            print("Valid Password")

        else:
            print("Invalid Password, Please enter valid password")

       #User password Rule 2

    def userpassword2(self):


            pattern6 = '^(?=.+[A-Z])[a-zA-Z0-9]{8,}$'
            userpassword = input("Enter the Password : ")
            if re.fullmatch(pattern6, userpassword):
                print("Valid Password")

            else:
                print("Invalid Password, Please enter valid password")

   #User passwor rule 3

    def userpassword3(self):

          # user password with atleast one numeric number
          
            pattern7='^(?=.+[A-Z])(?=.+[0-9])[a-zA-Z0-9]{8,}'
            userpassword = input("Enter the Password : ")
            if re.fullmatch(pattern7, userpassword):
                print("Valid Password")

            else:
                print("Invalid Password, Please enter valid password")

    # User passwor rule 4

    def userpassword4(self):

        # user password with atleast one special character number

        pattern8 = '^(?=.+[0-9])(?=.+[a-z])(?=.+[A-Z])(?=.+[@$#%*+]).{8,}$'

        userpassword = input("Enter the Password : ")
        if re.fullmatch(pattern8, userpassword):
            print("Valid Password")

        else:
            print("Invalid Password, Please enter valid password")


if __name__ == "__main__":
    user = UserRegistration()
    user.userfirstname()
    user.userlastname()
    user.user_email()
    user.usermobilenumber()
    user.userpassword()
    user.userpassword2()
    user.userpassword3()
    user.userpassword4()

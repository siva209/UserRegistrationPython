
class EmailTest:
    REGEX = '^[a-zA-Z0-9]+([.+-_][a-z-A-Z0-9]+)*@[a-zA-Z0-9]+.[a-z]{2,3}([.][a-z]{2,3})?$'
    # Valid Email Ids
    valid_email = [
        "abc@yahoo.com",
        "abc-100@yahoo.com",
        "abc.100@yahoo.com",
        "abc111@abc.com",
        "abc-100@abc.net",
        "abc.100@abc.com.au",
        "abc@1.com",
        "abc@gmail.com.com",
        "abc+100@gmail.com",
    ]
    # Invalid Email Ids
    invalid_email = [
        "abc@.com.my",
        "abc123@gmail.a",
        "abc123@.com",
        "abc123@.com.com",
        ".abc@abc.com",
        "abc()*@gmail.com",
        "abc..2002@gmail.com",
        "abc.@gmail.com",
        "abc@abc@gmail.com",
        "abc@gmail.com.1a",
        "abc@gmail.com.aa.au"
    ]

    # EMail Validation
    def email_validate(self, request):
        """
        :param request: i-Taking the emails from array (valid_email and invalid_email)
        :return: match email ids with respective regex pattern
        """
        return re.fullmatch(EmailTest.REGEX, request)


if __name__ == "__main__":
    email = EmailTest()
    print("....For Valid Email Ids....")
    for i in EmailTest.valid_email:
        test = bool(email.email_validate(i))
        print("Email id : " + i + " is valid :\t" + str(test))
    print("....For Invalid Email Ids....")
    for i in EmailTest.invalid_email:
        test = bool(email.email_validate(i))
        print("Email id : " + i + " is valid :\t" + str(test))
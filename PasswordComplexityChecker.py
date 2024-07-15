import re
def Password_Complexity(Password):
    if len(Password)<8:
        return('The password must be at least 8 characters long')
    elif not re.search("[A-Z]",Password):
        return("Password must contain at least one Uppercase letter")
    elif not re.search("[a-z]",Password):
        print("Password must contain at least one lowercase") 
    elif not re.search("[0-9]",Password):
        return("Password must contain at least one number")
    elif not re.search("[!@#$%^&*()_+={}\[\]:;\"'<>,.?/~`|-]",Password):
        return("Password must contain at least one special character")
    else:
        return("Your password is strong")


if __name__ == "__main__":
    Password = input("Create a password please: ")
    print(Password_Complexity(Password))
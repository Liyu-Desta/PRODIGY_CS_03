Password Complexity Checker 🔐
Project Overview 🎉
Welcome to the Password Complexity Checker project! This Python script is designed to ensure that user-generated passwords meet specific complexity requirements, enhancing security and making it more difficult for potential attackers to crack them. This project was developed as part of my internship at Prodigy InfoTech.

Features ✅
Checks for at least one uppercase letter 🅰️
Checks for at least one lowercase letter 🔡
Checks for at least one number 🔢
Checks for at least one special character 💥
Ensures a minimum length of 8 characters 📏
Getting Started 🚀
These instructions will help you set up and run the Password Complexity Checker on your local machine.

Prerequisites
Ensure you have Python installed on your system. You can download Python from python.org.

Installation
Clone the repository:

sh
Copy code
git clone https://github.com/Liyu-Desta/PRODIGY_CS_03.git
Navigate to the project directory:

sh
Copy code
cd password-complexity-checker
Usage
Run the PasswordComplexityChecker.py script to check the complexity of a password:

sh
Copy code
python PasswordComplexityChecker.py
The script will prompt you to enter a password and will provide feedback based on the following criteria:

At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character
A minimum length of 8 characters
Example
sh
Copy code
Create a password please: HelloWorld123!
Your password is strong
Code Explanation
The script uses the re module in Python to perform regular expression searches and ensure that the password meets all the required complexity criteria. Here's a brief overview of the code:

python
Copy code
import re

def Password_Complexity(password):
    if len(password) < 8:
        return 'The password must be at least 8 characters long'
    elif not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    elif not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter"
    elif not re.search("[0-9]", password):
        return "Password must contain at least one number"
    elif not re.search("[!@#$%^&*()_+={}\[\]:;\"'<>,.?/~`|-]", password):
        return "Password must contain at least one special character"
    else:
        return "Your password is strong"

if __name__ == "__main__":
    password = input("Create a password please: ")
    print(Password_Complexity(password))
Lessons Learned 📚
From this project, I've gained valuable insights into using the re package in Python for regular expressions. I've also learned about the importance of ensuring password security by using a variety of character types to make passwords more robust against attacks.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Prodigy InfoTech for the internship opportunity
The Python community for providing valuable resources and support
Thank You ! Happy coding!

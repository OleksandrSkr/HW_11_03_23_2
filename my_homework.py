#mail, login , password 
def registration (account):
    mail = input("Enter your mail. Mail must contain '@' and '.' : ")
    if "@" and "." not in mail:
        print("Incorrect mail. Mail must contain '@' and '.'")
    else:
        login = input("Enter your login. The login must be longer than two characters and begin with an uppercase letter: ")
#        first_letter = login[0]
#       print (first_letter)
#       print(login.upper()[0])
#        if first_letter != login.upper()[0] or len(login) < 2:
        if login[0] != login.upper()[0] or len(login) < 2:
            print("Incorrect login. The login must be longer than two characters and begin with an uppercase letter")
        else:
            password = input("Enter your passwopd. Password must be at least 6 characters long, contain uppercase and lowercase letters, as well as numbers and special characters : ")
            count_digit = 0
            count_lower = 0
            count_upper = 0
            count_spec = 0
            for i in password:
                if i.isdigit():
                    count_digit += 1

                if i.islower():
                    count_lower += 1

                if i.isupper():
                    count_upper += 1
                
                if i in "!@#$%^&*":
                    count_spec += 1

            if count_digit > 0 and count_lower > 0 and count_upper >0 and count_spec > 0:
                print("The password is secure")
                user = {
                    "mail": mail,
                    "login" : login,
                    "password" : password
                    },
                print(user)
                users.append(user)

            else:
                print("Password incorrect. Password must be at least 6 characters long, contain uppercase and lowercase letters, as well as numbers and special characters ")


user ={}
users = []

print("Hello, plese registration ")

registration(user)

print(users)



#user = 


#login = input("Enter login that you want to use continuously : ")
#password = input("Enter your password : ")
#balance = input("How much money do you want to send? : ")

#user = registration(login ,password, balance)



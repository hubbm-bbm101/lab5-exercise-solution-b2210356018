def is_valid(email):
    email = str(input("Write your e-mail."))
    if "@" in email:
        if "." in email:
            print("It is valid.")
    else:
        print("Not valid")
is_valid("")

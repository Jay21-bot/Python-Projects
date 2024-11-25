email = input("Enter your email address: ")

if "@" not in email or "." not in email:
    print("Please enter a valid email address")

username = email [:email.index("@")]

domain = email [email.index("@") + 1 :]

print(f" Your Username is : {username}")

print(f" Your Domain is : {domain}")
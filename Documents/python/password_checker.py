##Password Checker ##
username=input("Enter your username:")
password=input("Enter your password:")
length=len(password)
hidden_password='*' * length
print(f"Hey {username} , your password ,{hidden_password} ,is {length} long")

#task #2
username = input("Enter  your username: ") 
password = input("Enter your  password: ")
username = username.lower()
username = username.replace(" ", "_")
password_length = len(password) #فينا نعملها عن طريق for loop
print("Name:"+username)
print("Password:",password)
#task #2
username = input("Enter  your username: ") 
password = input("Enter your  password: ")
username = username.lower()
username = username.replace(" ", "_")
password_length = len(password) #فينا نعملها عن طريق for loop
print("Name:"+username)
print("Password:",password)
print("If the password length is greater than or equal to 8:", password_length >= 8)
print("If the username is admin:", username == "admin")
print("If the password is 1234:", password == "1234")
print("Check if it's default account → (username is \"admin\" and the password is \"1234\"):", username == "admin" and password == "1234")




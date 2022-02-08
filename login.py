# Opens the File With Western Log-in
data_file = open("data.txt", "r")

username = data_file.readline()
password = data_file.readline()

data_file.close()

# Prompt User to Check Existing Info / Input Proper Info
print("Is this information correct?\nUsername: {}Password: {}".format(
    username, password))
saved = int(input("1 - Yes, 0 - No: "))

# If Incorrect, Rewrite to File
if saved == 0:
    data_file = open("data.txt", "w")

    username = input("Username: ")
    data_file.write(username)
    data_file.write("\n")

    password = input("Password: ")
    data_file.write(password)

    print("Information Saved")
else:
    pass

# Open File with Authorized Pickup Person Information
pickup_file = open("pickup.txt", "r")

first = pickup_file.readline()
last = pickup_file.readline()
home = pickup_file.readline()
mobile = pickup_file.readline()
email = pickup_file.readline()

pickup_file.close()

# Prompt User to Check Existing Info / Input Proper Info
print("\nIs this information correct? \nFirst Name: {}Last Name: {}Home Phone: {}Mobile: {}Email: {}".format(
    first, last, home, mobile, email))
saved2 = int(input("1 - Yes, 0 - No "))

# If Incorrect, Rewrite to File
if saved2 == 0:
    pickup_file = open("pickup.txt", "w")

    first = input("First Name: ")
    pickup_file.write(first)
    pickup_file.write("\n")

    last = input("Last Name: ")
    pickup_file.write(last)
    pickup_file.write("\n")

    home = input("Home Phone: ")
    pickup_file.write(home)
    pickup_file.write("\n")

    mobile = input("Mobile: ")
    pickup_file.write(mobile)
    pickup_file.write("\n")

    email = input("Email: ")
    pickup_file.write(email)

    print("Information Saved")
else:
    pass

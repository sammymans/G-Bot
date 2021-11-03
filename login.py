#opens the file (read and write)
data_file= open("data.txt","r")

username= data_file.readline()
password=data_file.readline()

data_file.close()

print("Is this information correct?\nUsername: "+username+"Password: "+password)
saved = int(input("1 for Yes, 0 for No "))

if saved==0:
    data_file= open("data.txt","w")
    username= input("Username: ")
    data_file.write(username)
    data_file.write("\n")
    password= input("Password: ")   
    data_file.write(password)
    print("Information Saved")
else:
    print("OK")

pickup_file = open("pickup.txt", "r")

first = pickup_file.readline()
last =pickup_file.readline()
home = pickup_file.readline()
mobile =pickup_file.readline()
email = pickup_file.readline()

pickup_file.close()

print("Is this information correct? \nFirst Name: " + first + "\nLast Name: " + last + "\nHome Phone: " + home + "\nMobile: " + mobile + "\nEmail: " + email)
saved2 = int(input("1 for Yes, 0 for No "))

if saved2==0:
    pickup_file= open("pickup.txt","w")

    first= input("First Name: ")
    pickup_file.write(first)
    pickup_file.write("\n")

    last= input("Last Name: ")
    pickup_file.write(last)
    pickup_file.write("\n")
    
    home= input("Home Phone: ")
    pickup_file.write(home)
    pickup_file.write("\n")

    mobile= input("Mobile: ")
    pickup_file.write(mobile)
    pickup_file.write("\n")

    email= input("Email: ")
    pickup_file.write(email)
    
    print("Information Saved")
else:
    print("OK")




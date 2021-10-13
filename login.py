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
else:
    print("OK")






# Retrieve Options
sports = open("sportlist.txt")
sport_options = sports.readlines()

# Print Options to User
for x in sport_options:
    print(x)

# Take in Selected Sport
sport_picked = int(input("Which sport would you like to look at? Input the number: "))

# Acquire More Information if Squash
if sport_picked == 7:
    print("If you do not have a partner input N/A 3 times")
    fname= input("Name of partner: ")
    student_id = input("Partner student number: ")
    pemail =input("Partner email: ")

# Retrieve Links
sports_urls = open("sporturls.txt")
content = sports_urls.readlines()

# Save Proper Link
my_url= content[sport_picked-1]
print(my_url)
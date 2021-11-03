sports=open("sportlist.txt")
sportlist= sports.readlines()
i=0
for x in sportlist:
    print(sportlist[i])
    i+=1



sportpicked=int(input("Which sport would you like to look at? Input the number: "))

sportslist=open("sporturls.txt")

content= sportslist.readlines()

if sportpicked ==7:
    print("If you do not have a partner input N/A 3 times")
    fname= input("Name of partner: ")
    student_id = input("Partner student number: ")
    pemail =input("Partner email: ")






my_url= content[sportpicked-1]
print(my_url)
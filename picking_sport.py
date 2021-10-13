sports=open("sportlist.txt")
sportlist= sports.readlines()
i=0
for x in sportlist:
    print(sportlist[i])
    i+=1



sportpicked=int(input("Which sport would you like to look at? Input the number: "))

sportslist=open("sporturls.txt")

content= sportslist.readlines()





my_url= content[sportpicked-1]
print(my_url)
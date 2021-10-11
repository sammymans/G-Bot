import requests

from bs4 import BeautifulSoup

my_url= "https://shop.westernmustangs.ca/Program/GetProgramDetails?courseId=7fecf404-873b-44d2-bf86-1910051b3097&semesterId=81dac0e7-2456-44c9-bfe4-6ed494cc6824"

page= requests.get(my_url)

soup= BeautifulSoup(page.content, 'html.parser')

page.close()

containers =soup.findAll("div", {"class":"caption program-schedule-card-caption"})



for container in containers:

    Date= container.h4.span.text
    Time = container.h4.small.text
    Available=container.h4.small.span.text

    list = Time.split()
    
    newstr = ""
    i= 0
    while not list[i].isdigit():
        newstr += list[i]
        i += 1

    print(newstr)

    # list = Time.splitlines()
    # print(list)


    #print("Date: "+ Date.strip())
    #print("Time: "+ Time.strip())
    #print("Availability: "+ Available.strip())






import requests

from bs4 import BeautifulSoup

import picking_sport
import login

from picking_sport import my_url

page= requests.get(my_url)

soup= BeautifulSoup(page.content, 'html.parser')

page.close()

containers =soup.findAll("div", {"class":"caption program-schedule-card-caption"})
#for container in containers:
for count, container in enumerate(containers):

    Date= container.h4.span.text
    Time = container.h4.small.text
    Available=container.h4.small.span.text

    list = Time.split()

    times = ""
    i = 0
    while not list[i].isdigit() and i <= 4:
        times += list[i]
        i += 1

    print("\nOption " + str(count+1) + ":")
    print("Date: "+ Date.strip())
    print("Time: "+ times)
    print("Availability: "+ Available.strip())

time_Option= int(input("Which Option Would You Like?"))-1

print(time_Option)






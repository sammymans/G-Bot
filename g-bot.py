import requests

from bs4 import BeautifulSoup

import picking_sport
import login

from picking_sport import my_url

page= requests.get(my_url)

soup= BeautifulSoup(page.content, 'html.parser')

page.close()

containers =soup.findAll("div", {"class":"caption program-schedule-card-caption"})

for container in containers:

    Date= container.h4.span.text
    Time = container.h4.small.text
    Available=container.h4.small.span.text

    list = Time.split()
    
    times = ""
    i = 0
    while not list[i].isdigit():
        times += list[i]
        i += 1

    print("\nDate: "+ Date.strip())
    print("Time: "+ times)
    print("Availability: "+ Available.strip())






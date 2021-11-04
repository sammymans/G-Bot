import requests

from bs4 import BeautifulSoup

import pickSport
from pickSport import my_url

# Access Website With Ability to Parse
page = requests.get(my_url)
soup = BeautifulSoup(page.content, 'html.parser')
page.close()

# Save All Time Cards
containers = soup.findAll("div", {"class":"caption program-schedule-card-caption"})

# Print All Available Times
for count, container in enumerate(containers):

    date = container.h4.span.text
    time = container.h4.small.text
    available = container.h4.small.span.text

    list = time.split()

    times = ""

    i = 0
    while not list[i].isdigit() and i <= 4:
        times += list[i]
        i += 1

    print("\nOption " + str(count+1) + ":")
    print("Date: " + date.strip())
    print("Time: " + times)
    print("Availability: " + available.strip())

# Save Desired Time Option
time_option= int(input("Which Option Would You Like?"))-1
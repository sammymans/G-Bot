import requests

from bs4 import BeautifulSoup

import pickSport
from pickSport import my_url

# Access Website With Ability to Parse
page = requests.get(my_url)
soup = BeautifulSoup(page.content, 'html.parser')
page.close()

# Save All Time Cards
containers = soup.findAll("div", {"class": "card-body"})

# Print All Available Times
for count, container in enumerate(containers):

    date = container.p.text
    timenAvaibilbe = container.div.find_all("p")
    time = timenAvaibilbe[0].small.text
    available = timenAvaibilbe[1].small.text

    print("\nOption {}:".format(count+1))
    print("Date: " + date.strip())
    print("Time: " + time)
    print("Availability: " + available.strip())

# Save Desired Time Option
time_option = int(input("Which Option Would You Like?"))-1

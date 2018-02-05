import time
from datetime import datetime as dt

#Identifying location of host file(May vary between operating systems)
hostPath = r"C:\Windows\System32\drivers\etc\hosts"

#Redirect URL to localhost
redirect = "127.0.0.1"

#Websites we want to be blocked
websiteList = ("www.facebook.com", "facebook.com")

while True:
    #If between 8 am and 5 pm write to host file, so when one of our websiteList websites is encountered,
    #we redirect to our localhost
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) <  dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working Hours...")
        with open(hostPath, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        #If between 5 pm and 8 am erase localhost redirects,
        #so we can access our websiteList websites
        print("Free time!")
        with open(hostPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(60)

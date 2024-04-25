from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import regex as re
import time

# Note that this uses a while loop, so to cancel it just ctrl-c in the terminal

# URL of the UMD schedule of classes page after searching for the class
url = "https://app.testudo.umd.edu/soc/search?courseId=agst130&sectionId=&termId=202408&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"

# Position of the section you want, 0 indexed from the top
pos = 0

# Seconds between checks
timeBetweenChecks = 3600

while True:
    # Using Selenium to scrape the number of seats available for the class, then putting it into a beautiful soup object
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Regex for the data in a prettify function (Why there is a space)
    text = """<span class=\"open-seats-count\">
     *[0-9]+"""
    
    # Find all and return the one at position
    match = re.findall(text, soup.prettify())[pos]

    # Look for the number of seats available
    num = re.search("[0-9]+", match).group()
    if num != "0":
        print(num, "seats available!")
    else:
        print("no seats available")
    driver.close()

    # Repeat every timeBetweenChecks seconds
    time.sleep(timeBetweenChecks)
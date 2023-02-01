from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# get keyword from user input
gig_keyword = input("Enter the gig keyword: ")

# get username and password from user input
username = input("Enter your Fiverr username: ")
password = input("Enter your Fiverr password: ")

# install necessary packages
apt-get update && apt-get install -y libpangocairo-1.0-0 libx11-6 libx11-dev xorg

# install chrome browser and chrome driver
apt-get install wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
apt-get install -f

# install chromedriver
!wget https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!mv chromedriver /usr/local/bin/

# initialize Chrome driver
driver = webdriver.Chrome()

# navigate to Fiverr
driver.get("https://www.fiverr.com/")

# search for the keyword
search_box = driver.find_element_by_name("q")
search_box.send_keys(gig_keyword)
search_box.send_keys(Keys.RETURN)

# gather information about the results of the search
results = driver.find_elements_by_css_selector(".responsive-collapse-item.ng-scope")
recipients = []

# limit the number of recipients to 1000
for i in range(min(1000, len(results))):
    recipient = results[i].find_element_by_css_selector("a.seller-username").text
    recipients.append(recipient)

# navigate to the messaging platform (e.g. Fiverr messages)
driver.get("https://www.fiverr.com/messages/")

# log in to the platform
username_field = driver.find_element_by_id("email")
password_field = driver.find_element_by_id("password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.submit()

# send messages about the project requirement
keyword = input("Enter the project requirement: ")
message = "Hello! I came across your gig and I think you might be able to help me with a project I'm working on. It involves " + keyword + " and I would love to hear more about your experience and availability. Let me know if you're interested."

for recipient in recipients:
    # navigate to the recipient's messaging page
    driver.get("https://www.fiverr.com/messages/new?recipient=" + recipient)
    text_box = driver.find_element_by_xpath('//*[@id="new_message_body"]')
    text_box.send_keys(message)
    send_button = driver.find_element_

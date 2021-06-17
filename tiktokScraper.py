from os import link
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq #grab from the page
from bs4 import BeautifulSoup as soup #parse html text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq #grab from the page
from bs4 import BeautifulSoup as soup #parse html text

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/Users/idanlau/Downloads/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get('https://www.google.com/')

sub = "Lil Dicky"
search = driver.find_element_by_xpath("//input [@name = 'q']")
search.send_keys(sub)
search.send_keys(Keys.RETURN)

my_url = driver.current_url

#instagramUser = []
#while len(instagramUser) == 0:
# try:
    # instagramUser = driver.find_elements_by_xpath("//g-link[@class='fl']/a")
    # #instagramUser = driver.find_element_by_tag_name('a')
    # instagramUser = instagramUser.get_attribute('href')
# instagramUser = driver.find_elements_by_xpath("//div[@class='S6VXfe']/a")get_attribute(href)

    #instagramUser = instagramUser.text
# print("user")
# print(instagramUser)


lnks=driver.find_elements_by_tag_name("g-link")
lnks=lnks[2].find_elements_by_tag_name("a")
# traverse list
for lnk in lnks:
	# if "instagram" in str(lnk):
	# 	print(lnk.get_attribute("href"))
	print(lnk.get_attribute("href"))
	#print(lnk.get_attribute("href"))


driver.quit()
# except:
#     pass
# firstRes = instagramUser[0]
# firstRes.click()

# username = "bot404sugondeez"
# password = "3.1415926"

# search = driver.find_element_by_xpath("//input [@name = 'username']")
# search.send_keys(username)
# search.send_keys(Keys.RETURN)

# uClient = uReq(my_url) #opening up connection, grabbing the page
# page_html = uClient.read()#stores all content into a variable
# uClient.close()

# page_soup = soup(page_html, "html.parser")#html parsing
# #print(page_soup.h1)

# containers = page_soup.findAll("section", {"class":"zwlfE"}) #grabs each product
# #print(len(containers))

# for i in containers:
#     brand = div.h2
#     print("Insta Name: " + brand)
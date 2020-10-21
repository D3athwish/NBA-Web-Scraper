import time
from selenium import webdriver

#User inputs player name
userInput = input("Enter player name: ")

#Set geckodriver directory
driver = webdriver.Firefox(executable_path='D:\GeckoDriver\geckodriver.exe')

#Open nba stats website
driver.get("https://stats.nba.com/")

time.sleep(5)

#Click Cookie Policy accept button
clickAccept = driver.find_element_by_id("onetrust-accept-btn-handler")
clickAccept.click()

time.sleep(5)

#Click searchbox
selectElement = driver.find_element_by_class_name("stats-search__icon-text")
selectElement.click()

time.sleep(5)

#Input player into searchbox
inputSearch = driver.find_element_by_class_name("stats-search__input")
inputSearch.send_keys(userInput)

time.sleep(5)

#Click first result of player
clickResult = driver.find_element_by_class_name("stats-search__link-anchor")
clickResult.click()

time.sleep(5)

#Find number of rows in the Traditional Splits table
rowNumber = len(driver.find_elements_by_css_selector(".stats-splits > nba-stat-table:nth-child(8) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr")) + 1

#Loop over all of the rows and output date and 3PA scores
for x in range(1, rowNumber):
     elementDate = driver.find_element_by_xpath(
         "/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(x) + "]/td[1]")

     elementPA = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(x) +"]/td[10]")

     print(elementDate.text + " " + elementPA.text)

     print("\n")
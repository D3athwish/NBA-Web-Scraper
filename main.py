import time
from selenium import webdriver

#Uporabnik vnese ime igralca
userInput = input("Enter player name: ")

driver = webdriver.Firefox(executable_path='D:\GeckoDriver\geckodriver.exe')

#Driver zažene spodnji URL
driver.get("https://stats.nba.com/")

time.sleep(5)

#Driver klikne na accept gumb -> Privacy Policy
clickAccept = driver.find_element_by_id("onetrust-accept-btn-handler")
clickAccept.click()

time.sleep(5)

#Driver klikne na searchbox
selectElement = driver.find_element_by_class_name("stats-search__icon-text")
selectElement.click()

time.sleep(5)

#Driver vpiše uporabnika v searchbox
inputSearch = driver.find_element_by_class_name("stats-search__input")
inputSearch.send_keys(userInput)

time.sleep(5)

#Driver poišče uporabnika
clickResult = driver.find_element_by_class_name("stats-search__link-anchor")
clickResult.click()

time.sleep(5)

#Loop gre skozi 20 vrstic in vsako izpiše
for x in range(1, 20):
    elementDate = driver.find_element_by_xpath(
        "/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(x) + "]/td[1]")

    elementPA = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(x) +"]/td[10]")

    print(elementDate.text + " " + elementPA.text)

    print("\n")
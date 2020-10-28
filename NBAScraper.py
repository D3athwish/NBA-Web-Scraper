import time
from selenium import webdriver

# User inputs player name
userInput = input("Enter NBA player name: ")

# Set GeckoDriver directory
driver = webdriver.Firefox(executable_path='D:\GeckoDriver\geckodriver.exe')

# Open NBA players website, instead of nba stats due to website change
driver.get("https://www.nba.com/players")

time.sleep(10)

# Click Cookie Policy accept button
clickAccept = driver.find_element_by_id("onetrust-accept-btn-handler")
clickAccept.click()

time.sleep(10)

# Click searchbox to start searching
searchBox = driver.find_element_by_class_name("border")
searchBox.click()

time.sleep(10)

# Input player name into searchbox
searchBox.send_keys(userInput)

time.sleep(10)

# Click first result
clickResult = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/section/div/div[2]/div["
                                           "2]/div/div/div/table/tbody/tr/td[1]/a/div[2]/p[1]")
clickResult.click()

time.sleep(10)

# Click stats button to navigate to NBA players stats
clickStatsButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[1]/div/ul/li[2]/a")
clickStatsButton.click()

time.sleep(10)

# Find number of rows in the Traditional Splits table
rowNumber = len(driver.find_elements_by_css_selector(
    "nba-stat-table.stats-table-next:nth-child(8) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > "
    "tbody:nth-child(2) > tr")) + 1

# Loop over all of the rows and output date and 3PA scores
for x in range(1, rowNumber):
    elementDate = driver.find_element_by_xpath(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(x) +
        "]/td[1]")

    elementPA = driver.find_element_by_xpath(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(x) +
        "]/td[10]")

    print(elementDate.text + " " + elementPA.text)

    print("\n")

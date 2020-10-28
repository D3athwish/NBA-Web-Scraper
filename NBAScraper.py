import time
from selenium import webdriver


def x_path_with_click(string):
    time.sleep(10)
    return driver.find_element_by_xpath(string)


def x_path(string):
    return driver.find_element_by_xpath(string)


def element_Id_with_click(string):
    time.sleep(10)
    return driver.find_element_by_id(string).click()


def element_class_with_click(string):
    time.sleep(10)
    return driver.find_element_by_class_name(string).click()

# User inputs player name
userInput = input("Enter NBA player name: ")

# Set GeckoDriver directory
driver = webdriver.Firefox()

# Open NBA players website, instead of nba stats due to website change
driver.get("https://www.nba.com/players")
time.sleep(10)

# Click Cookie Policy accept button
clickAccept = element_Id_with_click("onetrust-accept-btn-handler")

# Click searchbox to start searching
searchBox = element_class_with_click("border")

# Input player name into searchbox
searchBox.send_keys(userInput)

# Click first result
clickResult = x_path_with_click("/html/body/div[1]/div[2]/div[3]/section/div/div[2]/div["
                                "2]/div/div/div/table/tbody/tr/td[1]/a/div[2]/p[1]")

# Click stats button to navigate to NBA players stats
clickStatsButton = x_path_with_click("/html/body/div[1]/div[2]/div[3]/div/div[1]/div/ul/li[2]/a")

# Find number of rows in the Traditional Splits table
rowNumber = len(driver.find_elements_by_css_selector(
    "nba-stat-table.stats-table-next:nth-child(8) > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > "
    "tbody:nth-child(2) > tr")) + 1

# Loop over all of the rows and output date and 3PA scores
for _ in range(1, rowNumber):
    elementDate = x_path(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(_) +
        "]/td[1]")

    elementPA = x_path(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(_) +
        "]/td[10]")

    print(elementDate.text + " " + elementPA.text)

    print("\n")
import time
from selenium import webdriver


def x_path(string):
    time.sleep(10)
    return driver.find_element_by_xpath(string)


def element_id(string):
    time.sleep(10)
    driver.find_element_by_id(string).click()
    return ""


def element_class(string):
    time.sleep(10)
    return driver.find_element_by_class_name(string).click()


def get_row_number():
    return len(driver.find_elements_by_css_selector("nba-stat-table.stats-table-next:nth-child(8) > div:nth-child(2) "
                                                    "> div:nth-child(1) > table:nth-child(1) > "
                                                    "tbody:nth-child(2) > tr")) + 1


# User inputs player name
userInput = input("Enter NBA player name: ")

# Set GeckoDriver directory
driver = webdriver.Firefox()

# Open NBA players website, instead of nba stats due to website change
driver.get("https://www.nba.com/players")

# Click Cookie Policy accept button
element_id("onetrust-accept-btn-handler")

# Click searchbox to start searching, and input player name into searchbox
element_class("border").send_keys(userInput)

# Click first result
x_path("/html/body/div[1]/div[2]/div[3]/section/div/div[2]/div["
       "2]/div/div/div/table/tbody/tr/td[1]/a/div[2]/p[1]").click()

# Click stats button to navigate to NBA players stats
x_path("/html/body/div[1]/div[2]/div[3]/div/div[1]/div/ul/li[2]/a").click()

# Get number of rows and loop over them
for _ in range(1, get_row_number()):
    elementDate = x_path(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(_) +
        "]/td[1]")

    elementPA = x_path(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(_) +
        "]/td[10]")

    print(elementDate.text + " " + elementPA.text + "\n")
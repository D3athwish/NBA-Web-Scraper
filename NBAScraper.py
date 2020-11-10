from selenium import webdriver
import time


def x_path(string):
    time.sleep(10)
    return driver.find_element_by_xpath(string)


def check_for_cookie_popups(string):
    time.sleep(10)
    try:
        driver.find_element_by_id(string).click()
    except Exception:
        pass


def element_class(string, user):
    time.sleep(10)
    driver.find_element_by_class_name(string).send_keys(user)
    return 0


def check_for_popups(button1):
    try:
        x_path(button1).click()
    except Exception:
        pass


# User inputs player name
userInput = input("Enter NBA player name: ")

# Open Firefox
driver = webdriver.Firefox()

# Open NBA players website, instead of nba stats due to website change
driver.get("https://www.nba.com/players")

# Click Cookie Policy accept button
check_for_cookie_popups("onetrust-accept-btn-handler")

# Click searchbox to start searching, and input player name into searchbox
element_class("border", userInput)

# Click first result
x_path("/html/body/div[1]/div[2]/div[3]/section/div/div[2]/div["
       "2]/div/div/div/table/tbody/tr/td[1]/a/div[2]/p[1]").click()

# Check if popup is present, if it is close it, if not pass
check_for_popups("/html/body/div[4]/div[2]/button")
check_for_popups("/html/body/div[3]/div[2]/button")
check_for_popups("/html/body/div[2]/div[2]/button")

# Click stats button to navigate to NBA players stats
x_path("/html/body/div[1]/div[2]/div[3]/div/div[1]/div/ul/li[2]/a").click()

time.sleep(10)

# Get number of rows
row_number_string = "nba-stat-table.stats-table-next:nth-child(8) > div:nth-child(2)> div:nth-child(1) > " \
                    "table:nth-child(1) > tbody:nth-child(2) > tr"
row_number = len(driver.find_elements_by_css_selector(row_number_string)) + 1

# Loop over rows
for _ in range(1, row_number):
    elementDate = driver.find_element_by_xpath("/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table["
                                               "1]/div[2]/div[1]/table/tbody/tr[" + str(_) + "]/td[1]")

    elementPA = driver.find_element_by_xpath(
        "/html/body/main/div/div/div/div[4]/div/div/div/div/nba-stat-table[1]/div[2]/div[1]/table/tbody/tr[" + str(_) +
        "]/td[10]")

    print(elementDate.text + " " + elementPA.text + "\n")

driver.close()

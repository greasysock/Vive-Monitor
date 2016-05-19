from selenium import webdriver
#planning to implement htcvive.com in the future.
def findmyorder(ordernumber, password):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("https://www.findmyorder.com")
    driver.find_element_by_name("orderNumber").send_keys(ordernumber)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("dr_button").click()
    return driver.page_source.encode('ascii','ignore')
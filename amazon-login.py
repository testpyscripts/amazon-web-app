from selenium import webdriver 
import time
from selenium.webdriver.common.key import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service 

driver=webdiver.Chrome(executable_path="C:\Program Files\Python310\chromedriver")


driver.get("https://www.amazon.in/") #open amazon web app
driver.maximize_window()
time.sleep(7)                         # sleep 5 sc
driver.find_element_by_name("textusername").send_keys("pvsai777")
driver.find_element_by_name("testpassword").send_keys("PVsai777***")
driver.find_element_by_name("submit").click()        # amazon login 

driver.find_element(By.XPATH,//*[@id="CardInstanceuBltTpKT4UXVqDMgDi68Pg"]/div[1]/div[2]/div[1]/div/div[1]/a/div/img").click() # search a product 
time.sleep(7)

select_qa=select(driver.find_element(By.Id,"quantity")) # select the quntity
select_qa.select_by_index(1)
time.sleep(7)

driver.find_element_by_name("submit.add-to-cart").click() #add to cart 
time.sleep(7)

driver.(By.XPATH,//*[@id="CardInstanceuBltTpKT4UXVqDMgDi68Pg"]/div[1]/div[2]/div[1]/div/div[1]/a/div/img").remove()


driver.close() # close the browser
driver.quit() # quit all browsers



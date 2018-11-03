from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/sshussai/chromedriver")
#driver = webdriver.Chrome("/mnt/c/Users/sshussai/Downloads/chromedriver_win32")
driver.get('http://127.0.0.1:8000')
nameText = driver.findElement(By.id('name').getText())
aboutText = driver.findElement(By.id('about').getText())
skillsText = driver.findElement(By.id('skills').getText())
workText = driver.findElement(By.id('work').getText())
contactText = driver.findElement(By.id('contact').getText())
assert nameText != ""
assert aboutText != ""
assert skillsText != ""
assert workText != ""
assert contactText != ""


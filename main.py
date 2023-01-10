from selenium import webdriver
import time

def get_driver():
  # Set option to make browsing easier
  # create options using webdriver.ChromeOptions
  options = webdriver.ChromeOptions()
  # infobar may interfere with the script so disable it
  options.add_argument("disable-infobars")
  # start the browser as maximized.
  options.add_argument("start-maximized")
  # to avoid some issues that occur when you interact with a browser on a Linux computer
  options.add_argument("disable-dev-shm-usage")
  # disable browser security
  options.add_argument("no-sandbox")
  # to help selenium to avoid detection from the browser
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/")
  return driver

def clean_text(text):
  '''Extract only the temperature from text'''
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())